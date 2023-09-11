import math

from items.abstract_item import AbstractItem
from renderer.utils import LineWidth, Color
from utils.settings import CENTER_POINT


class ThorSphericalItem(AbstractItem):

    @property
    def get_total_height(self):
        total_height = self._spherical_height + self.data.s + self.data.h
        return total_height

    @property
    def get_total_diameter(self):
        mean_D = self.data.D - self.data.s
        mean_r = self.data.r + self.data.s / 2
        mean_R = self.data.R + self.data.s / 2
        t1 = math.asin((mean_D / 2 - mean_r) / (mean_R - mean_r)) * (180 / math.pi)
        t2 = 90 - t1
        krp = (2 * mean_r * math.pi / 360) * t2 * 2
        spp = (2 * mean_R * math.pi / 360) * 2 * t1
        Dz = krp + spp + 2 * self.data.h
        # Диаметр заготвки днища
        return Dz

    @property
    def get_total_weight(self):
        weight = math.pow(self.get_total_diameter, 2) * math.pi * 0.25 * self.data.s * self._density
        # Масса
        return weight

    @property
    def get_total_pressure(self):
        pressure = (2 * (self.data.s - self._get_c) * self._get_f * self._get_q) / \
                   (self._get_R + 0.5 * (self.data.s - self._get_c))
        # Давление
        return pressure

    @property
    def get_k(self):
        # Расчетная толщина стенки обечайки [мм]
        # sр = p * R / (2 * φ * [σ] - 0.5 * p)
        sp = self.data.p * self._get_R / (2 * self._get_f * self._get_q - 0.5 * self.data.p)

        # Расчетная толщина обечайки с учетом прибавок
        # sр + c = 3.25 + 1.5 = 4.75
        # Коэффициент запаса прочности днища
        k = self.data.s / (sp + self._get_c)
        return k

    @property
    def _get_c(self):
        # Прибавка на коррозию [мм]
        c1 = self.data.c1
        # Компенсация минусового допуска [мм]
        c2 = self.c2
        # Технологическая прибавка [мм]
        c3 = self.data.s * 0.15
        # Суммарная прибавка к толщине стенки обечайки [мм]
        c = c1 + c2 + c3
        return c

    @property
    def _get_R(self):
        R = pow(self._id, 2) / (4 * self.get_total_height)
        return R

    @property
    def _spherical_height(self):
        spherical_height = self.data.R - math.sqrt(
            math.pow(self.data.R - self.data.r, 2)
            - math.pow(self._id / 2 - self.data.r, 2)
        )
        return spherical_height

    @property
    def _title_template(self):
        return [
            self.data.D,
            self.data.R,
            self.data.r,
            self.data.h,
            self.data.s,
        ]

    @property
    def _angle(self):
        return math.acos((self.data.D / 2 - self.data.r - self.data.s) / (self.data.R - self.data.r))

    @property
    def _angle1(self):
        return math.asin(self.data.d / 2 / self.data.R)

    @property
    def _height_R(self):
        return math.tan(self._angle) * (self.data.D / 2 - self.data.r - self.data.s)

    @property
    def _height1(self):
        return math.tan(math.pi / 2 - self._angle1) * self.data.d / 2

    @property
    def _height(self):
        return self._height_R - math.cos(self._angle1) * self.data.R

    def draw(self, drawer):
        drawer.context.save()
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        L1 = ((-self.data.D / 2 + self.data.s) / self.scale, self.data.h / self.scale)
        R1 = ((self.data.D / 2 - self.data.s) / self.scale, self.data.h / self.scale)
        L2 = (-self.data.D / self.scale / 2, self.data.h / self.scale)
        R2 = (self.data.D / self.scale / 2, self.data.h / self.scale)
        L3 = ((-self.data.D / 2 + self.data.s) / self.scale, 0)
        R3 = ((self.data.D / 2 - self.data.s) / self.scale, 0)
        L4 = (-self.data.D / self.scale / 2, 0)
        R4 = (self.data.D / self.scale / 2, 0)
        L5 = (-self.data.d / 2 / self.scale, self._height / self.scale)
        R5 = (self.data.d / 2 / self.scale, self._height / self.scale)
        L6 = (-self.data.d / 2 / self.scale, (self._height - self.data.s) / self.scale)
        R6 = (self.data.d / 2 / self.scale, (self._height - self.data.s) / self.scale)
        AL = ((-self.data.D / 2 + self.data.r + self.data.s) / self.scale, 0)
        AR = ((self.data.D / 2 - self.data.r - self.data.s) / self.scale, 0)
        A0 = (0, self._height_R / self.scale)
        H0 = (R2[0], R6[1])
        drawer.poly_line([
            (0, self.data.h / self.scale),
            L1,
            L3])

        drawer.arc(*AL, self.data.r / self.scale, math.pi, math.pi + self._angle)
        drawer.arc(*A0, self.data.R / self.scale, math.pi + self._angle, -math.pi / 2 - self._angle1)
        drawer.stroke()

        # Рисуем левую половинку, внутреннюю часть
        drawer.poly_line([L1, L2, L4])
        drawer.arc(*AL, (self.data.r + self.data.s) / self.scale, math.pi, math.pi + self._angle)
        drawer.arc(*A0, (self.data.R + self.data.s) / self.scale, math.pi + self._angle, - math.pi / 2 - self._angle1)
        drawer.stroke()

        # Рисуем правую половинку
        drawer.poly_line([(0, self.data.h / self.scale), R1, R3])
        drawer.arc_negative(*AR, self.data.r / self.scale, 0, -self._angle)
        drawer.arc_negative(*A0, self.data.R / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()

        # Рисуем правую половинку, внутреннюю часть
        drawer.poly_line([R1, R2, R4])
        drawer.arc_negative(*AR, (self.data.r + self.data.s) / self.scale, 0, -self._angle)
        drawer.arc_negative(*A0, (self.data.R + self.data.s) / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.data.d > 0:
            drawer.line(L5, R5)
            drawer.line(R5, R6)
            drawer.line(R6, L6)
            drawer.line(L6, L5)
            drawer.stroke()

        # Размер D
        drawer.dimension(L2, R2, f'⌀{self.data.D}±2', 10)  # ⌀
        # drawer.dimension_diameter(L1, R1, f'{self.D}±2', 10)  # ⌀

        # Размер s
        drawer.dimension(R1, R2, f'{self.data.s}', 5, 'right', 'out')

        # Размер h
        if self.data.h > 0:
            drawer.dimension(L4, L2, f'{self.data.h}*', 5, 'right', 'out')

        # Размер d
        if self.data.d > 0:
            drawer.dimension(L6, R6, f'⌀{self.data.d}*', -10, 'right', 'out')
            # drawer.dimension_diameter(L6, R6, f'{self.d}*', -10, 'right', 'out')

        # Размер H
        H = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R6, H0)
        drawer.stroke()
        drawer.dimension(H0, R2, f'{H}±10', -10, 'center', 'in')

        # Размер r
        if self.data.r > 0:
            drawer.radius_dimension(AL, self.data.r / self.scale, f'r{self.data.r}', self._angle / 2, offset=5)

        # Размер R
        drawer.radius_dimension(
            A0,
            self.data.R / self.scale,
            f'R{self.data.R}',
            angle=(self._angle / 2 + math.pi / 4 - self._angle1),
            offset=5
        )

        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()
