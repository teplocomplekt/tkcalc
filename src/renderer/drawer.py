import math

import cairo

from renderer.utils import LineWidth, Color, matrix_multiplication
from utils.settings import FONT, BASE_DIR


class Drawer:
    def __init__(self, render):
        self.render = render
        self.context = self.render.context
        self.context.translate(0, -297)

        # Фон
        self.context.set_source_rgb(*Color.WHITE)
        self.context.rectangle(0, 0, 210, 297)
        self.context.fill()

        self.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        # self.context.select_font_face(FONT, cairo.FONT_SLANT_OBLIQUE, cairo.FONT_WEIGHT_NORMAL)
        self.context.select_font_face(FONT, cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)

        self.draw_watermark()

    def draw_watermark(self):
        self.context.save()

        try:
            img_surface = cairo.ImageSurface.create_from_png(BASE_DIR / 'logo_1000x282.png')

            image_size_width = img_surface.get_width()
            image_size_height = img_surface.get_height()

            scale = 100
            offset_factor = 700

            self.context.scale(scale / image_size_width, scale / image_size_width)
            self.context.rotate(math.radians(45))

            for x in range(0, 6, 2):
                for y in range(-2, 4, 1):

                    self.context.save()

                    offset_x = x*offset_factor + y*offset_factor/2
                    offset_y = y*offset_factor

                    self.context.translate(offset_x, offset_y)

                    self.red_dot((0, 0), '0,0')
                    self.red_dot((image_size_width, 0), f'{image_size_width},{0}')
                    self.red_dot((0, image_size_height), f'{0},{image_size_height}')
                    self.red_dot((image_size_width, image_size_height), f'{image_size_width},{image_size_height}')

                    self.context.transform(cairo.Matrix(yy=-1))
                    self.context.set_source_surface(img_surface, 0, -image_size_height)

                    self.context.paint()

                    self.context.restore()


        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")

        self.context.restore()

    def get_coordinates(self, point):
        x = point[0]
        y = point[1]
        return x, y

    def set_line_style(self, width, color):
        self.context.set_source_rgb(*color)
        self.context.set_line_width(width)

    def poly_line(self, points: list):
        self.context.move_to(*self.get_coordinates(points[0]))
        for point in points[1:]:
            self.context.line_to(*self.get_coordinates(point))

    def line(self, start_point, end_point):
        self.poly_line([start_point, end_point])

    def stroke(self):
        self.context.stroke()

    def arc(self, x, y, r, a1, a2):
        self.context.arc(*self.get_coordinates((x, y)), r, a1, a2)

    def arc_negative(self, x, y, r, a1, a2):
        self.context.arc_negative(*self.get_coordinates((x, y)), r, a1, a2)
        self.context.stroke()

    def red_dot(self, coordinates, text=''):
        self.context.save()
        self.context.translate(*self.get_coordinates((coordinates[0], coordinates[1])))
        self.context.set_source_rgb(0.9, 0.1, 0.1)
        self.context.arc(0, 0, 10, 0, 2 * math.pi)
        self.context.fill()
        self.context.stroke()
        self.context.set_source_rgb(0, 0, 0)
        self.text(text, 20, (0, 0))
        self.context.stroke()
        self.context.restore()

    def text(self, text, size, coordinates, align='left', angle=0, scale=1):

        self.context.save()
        self.context.translate(*self.get_coordinates((coordinates[0], coordinates[1])))
        self.context.transform(cairo.Matrix(yy=-1))
        self.context.set_font_size(size)

        (x, y, width, height, dx, dy) = self.context.text_extents(text)

        self.context.rotate(angle)
        self.context.scale(scale, 1)

        if align == 'right':
            self.context.translate(-width, 0)
        elif align == 'center':
            self.context.translate(-width / 2, 0)

        self.context.show_text(text)
        self.context.stroke()

        self.context.restore()

        return width, height

    def dimension(self, point1, point2, text, offset=5, align='center', arrow='in'):

        offset1 = 1.5
        text_padding = 2
        arrow_length = 2.5
        arrow_padding = 0 if arrow == 'in' else arrow_length + 1

        self.context.save()

        # Вычисляем угол наклона размера
        p = [[point2[0] - point1[0]], [point2[1] - point1[1]]]
        angle = math.pi / 2 - math.atan2(p[0][0], p[1][0])

        matrix = [
            [math.cos(-angle), -math.sin(-angle)],
            [math.sin(-angle), math.cos(-angle)]
        ]

        # координаты конечной точки в пространстве размера
        p1 = matrix_multiplication(matrix, p)
        p1 = p1[0][0], p1[1][0]

        self.context.translate(*point1)
        self.context.rotate(angle)

        self.set_line_style(LineWidth.THIN, Color.BLACK)

        # Рисуем стрелки
        self.context.save()
        self.context.translate(0, offset)
        if arrow != 'in':
            self.arrow(length=arrow_length, angle=math.pi)
        else:
            self.arrow(length=arrow_length)
        self.context.translate(*p1)
        if arrow != 'in':
            self.arrow(length=arrow_length)
        else:
            self.arrow(length=arrow_length, angle=math.pi)
        self.context.restore()

        # Рисуем выноски
        self.context.save()
        if offset > 0:
            self.line((0, 0), (0, offset + offset1))
            self.context.translate(*p1)
            self.line((0, 0), (0, offset + offset1))
        else:
            self.line((0, 0), (0, offset - offset1))
            self.context.translate(*p1)
            self.line((0, 0), (0, offset - offset1))
        self.stroke()
        self.context.restore()

        # Текст
        self.context.save()
        if align == 'left':
            self.context.translate(0, offset)
            width, height = self.text(text, 7, (-text_padding - arrow_padding, 1), 'right')
            self.line((-width - text_padding * 2 - arrow_padding, 0), p1)
            self.stroke()

        elif align == 'right':
            self.context.translate(0, offset)
            width, height = self.text(text, 7, (p1[0] + text_padding + arrow_padding, 1), 'left')
            self.line((0, 0), (p1[0] + width + text_padding * 2 + arrow_padding, 0))
            self.stroke()
        else:
            self.context.translate(0, offset)
            self.text(text, 7, (p1[0] / 2, 1), 'center')
            self.line((-arrow_padding, 0), (p1[0] + arrow_padding, 0))
            self.stroke()

        self.context.restore()
        self.context.restore()

    def arrow(self, length=2.5, r=1, angle=0.0):

        self.context.save()
        self.context.rotate(angle)
        l1 = math.tan(math.radians(10)) * length
        theta = math.asin(l1 / r)
        l2 = 1 / math.tan(theta) * l1
        self.context.move_to(length, l1)
        self.context.line_to(0, 0)
        self.context.line_to(length, -l1)
        self.context.arc_negative(length + l2, 0, r, math.pi + theta, math.pi - theta)
        self.context.fill()
        self.stroke()

        self.context.restore()

    def radius_dimension(self, center, radius, text, angle, offset=3):

        text_padding = 2
        arrow_length = 2.5
        arrow_padding = arrow_length + 1

        self.context.save()
        self.context.translate(*center)
        # Центр
        # self.line((-1, 0), (1, 0))
        # self.line((0, -1), (0, 1))
        # self.stroke()
        self.context.rotate(angle)
        self.context.translate(-radius, 0)
        self.arrow()
        width, height = self.text(text, 7, (-text_padding - offset, 1), 'right')
        self.line((arrow_padding, 0), (-text_padding * 2 - offset - width, 0))
        self.stroke()

        self.context.restore()

    def dimension_thickness(self, center, radius, thickness, text, angle, offset=3):

        text_padding = 2
        arrow_length = 2.5
        arrow_padding = arrow_length + 1

        self.context.save()
        self.set_line_style(LineWidth.THIN, Color.BLACK)
        self.context.translate(*center)
        # Центр
        # self.line((-1, 0), (1, 0))
        # self.line((0, -1), (0, 1))
        # self.stroke()
        self.context.rotate(angle)
        self.context.translate(-radius, 0)
        self.arrow()
        width, height = self.text(text, 7, (-text_padding - offset - thickness, 1), 'right')
        self.line((arrow_padding, 0), (-text_padding * 2 - offset - thickness - width, 0))
        # self.stroke()
        # self.context.translate(-thiknes, 0)
        # self.arrow(angle=math.pi)
        self.stroke()
        self.context.translate(-thickness, 0)
        self.arrow(angle=math.pi)

        self.context.restore()

    def dimension_angle(self, center, radius, angle1, angle2, text):
        self.context.save()
        self.set_line_style(LineWidth.THIN, Color.BLACK)
        self.context.translate(*center)

        self.arc_negative(0, 0, radius, angle1, angle2)

        width, height = self.text(f'{text}', 7, (0, radius + 3), align='center')

        self.context.save()
        self.context.rotate(angle1)
        self.context.translate(radius, 0)
        self.arrow(angle=-math.pi / 2)
        self.context.restore()

        self.context.rotate(angle2)
        self.context.translate(radius, 0)
        self.arrow(angle=math.pi / 2)

        # self.text(f'{text}°', 7, (0, radius + 5), align='center')
        self.stroke()

        self.context.restore()
