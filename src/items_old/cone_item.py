import math
from items_old.base_item import BaseItem, my_logger
from render.drawer import CENTER_POINT
from render.utils import LineWidth, Color
from utils.settings import CONE_VALUES


class ConeItem(BaseItem):

    @property
    def _title_template(self):
        return [
            self._id,
            self.Dm,
            self.r,
            self.h,
            self.s
        ]

    @property
    def get_total_height(self):
        r = self.r + self.s
        result = self.h
        result += r * math.sin(self.alpha / 2)
        result += ((self.D / 2 - r) + r * math.cos(self.alpha / 2) - self.Dm / 2) / math.tan(self.alpha / 2)
        return result

    @property
    def get_total_diameter(self):
        mean_D = self.D - self.s
        mean_r = self.r + self.s / 2
        if self.alpha == math.pi / 3:
            L = 2 * self.h + 1.92 * mean_D + 1.05 * mean_r
            return L
        if self.alpha == math.pi / 2:
            L = 2 * self.h + 1.289 * mean_D + 1.57 * mean_r
            return L
        my_logger.info('Формула расчета диаметра не применима')
        return 0

    @property
    def get_total_weight(self):
        if self.alpha == math.pi / 3:
            b = 180
            mean_d = self.d + 0.86 * self.s
            L1 = 2 * mean_d
        elif self.alpha == math.pi / 2:
            b = 254.31
            mean_d = self.d + 0.71 * self.s
            L1 = 1.414 * mean_d
        else:
            my_logger.info('Формула расчета веса не применима')
            return 0
        area = 0.785 * (pow(self.get_total_diameter, 2) - pow(L1, 2)) * b / 360
        weight = area * self.s * self.density
        return weight

    @property
    def get_k(self):
        sp = (self.p * self._id / (2 * self._get_Q * self._get_f - self.p)) * 1 / math.cos(self.alpha / 2)
        k = self.s / (sp + self._get_c)
        return k

    @property
    def get_total_pressure(self):
        # Согласно ГОСТ 34233.2-2017 Сосуды и аппараты. Нормы и методы расчета на прочность.

        # Применимость:
        # 0.001 ≤ s * cos(α) / D ≤ 0.050 && a > 70*
        if not (0.001 <= self.s * math.cos(self.alpha) / self._id <= 0.050) and self.alpha <= math.radians(70):
            my_logger.info('Формула расчета давления не применима (0.001 ≤ s * cos(α) / D ≤ 0.050)')

        # Допускаемое внутреннее избыточное давление [МПа]
        # [p] = 2 * [σ] * φр * (s - c) / (Dκ / cos(α) + (s - c))
        pressure = 2 * self._get_Q * self._get_f * (self.s - self._get_c) / (
                self._id / math.cos(self.alpha / 2) + (self.s - self._get_c))
        return pressure

    def draw(self, drawer):

        alpha = self.alpha
        drawer.context.save()
        # Смещаем начало координат в центр днища, центр листа
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)

        # Рассчитываем координаты для рисования
        L1 = (-self._id / self.scale / 2, self.h / self.scale)
        R1 = (self._id / self.scale / 2, self.h / self.scale)

        L2 = ((-self._id / 2 - self.s) / self.scale, self.h / self.scale)
        R2 = ((self._id / 2 + self.s) / self.scale, self.h / self.scale)

        L3 = (-self._id / self.scale / 2, 0)
        R3 = (self._id / self.scale / 2, 0)

        L4 = ((-self._id / 2 - self.s) / self.scale, 0)
        R4 = ((self._id / 2 + self.s) / self.scale, 0)

        AL = ((-self._id / 2 + self.r) / self.scale, 0)
        AR = ((self._id / 2 - self.r) / self.scale, 0)

        L5 = (AL[0] - (self.r / self.scale) * math.cos(alpha / 2), AL[1] - (self.r / self.scale) * math.sin(alpha / 2))
        R5 = (AR[0] + (self.r / self.scale) * math.cos(alpha / 2), AR[1] - (self.r / self.scale) * math.sin(alpha / 2))

        L6 = (AL[0] - ((self.r + self.s) / self.scale) * math.cos(alpha / 2),
              AL[1] - ((self.r + self.s) / self.scale) * math.sin(alpha / 2))
        R6 = (AR[0] + ((self.r + self.s) / self.scale) * math.cos(alpha / 2),
              AR[1] - ((self.r + self.s) / self.scale) * math.sin(alpha / 2))

        L7 = (-self.Dm / 2 / self.scale, (L5[0] + self.Dm / 2 / self.scale) / math.tan(alpha / 2) + L5[1])
        R7 = (self.Dm / 2 / self.scale, -(R5[0] - self.Dm / 2 / self.scale) / math.tan(alpha / 2) + R5[1])

        L8 = ((-self.Dm / 2 - math.cos(alpha / 2) * self.s) / self.scale,
              (L5[0] + self.Dm / 2 / self.scale) / math.tan(alpha / 2) + L5[1] - math.sin(
                  alpha / 2) * self.s / self.scale)
        R8 = ((self.Dm / 2 + math.cos(alpha / 2) * self.s) / self.scale,
              (L5[0] + self.Dm / 2 / self.scale) / math.tan(alpha / 2) + L5[1] - math.sin(
                  alpha / 2) * self.s / self.scale)

        H0 = (R2[0], R8[1])
        A0 = (0, L5[0] / math.tan(alpha / 2) + L5[1])

        # # Рисуем левую половинку, внутреннюю часть
        drawer.poly_line([(0, self.h / self.scale), L1, L3])
        drawer.arc(*AL, self.r / self.scale, math.pi, math.pi + alpha / 2)
        drawer.line(L5, L7)
        drawer.stroke()

        # Рисуем левую половинку
        drawer.poly_line([L1, L2, L4])
        drawer.arc(*AL, (self.r + self.s) / self.scale, math.pi, math.pi + alpha / 2)
        drawer.line(L6, L8)
        drawer.stroke()

        # # Рисуем правую половинку, внутреннюю часть
        drawer.poly_line([(0, self.h / self.scale), R1, R3])
        drawer.arc_negative(*AR, self.r / self.scale, 0, -alpha / 2)
        drawer.line(R5, R7)
        drawer.stroke()

        # # Рисуем правую половинку
        drawer.poly_line([R1, R2, R4])
        drawer.arc_negative(*AR, (self.r + self.s) / self.scale, 0, -alpha / 2)
        drawer.line(R6, R8)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.d > 0:
            drawer.line(L8, L7)
            drawer.line(L7, R7)
            drawer.line(R7, R8)
        drawer.line(R8, L8)
        drawer.stroke()

        # Размер D
        drawer.dimension(L2, R2, f'⌀{self.D}±2', 10)  # ⌀
        # drawer.dimension_diameter(L1, R1, f'{self.D}±2', 10)  # ⌀

        # Размер s
        drawer.dimension(R1, R2, f'{self.s}', 5, 'right', 'out')

        # Размер h
        if self.h > 0:
            drawer.dimension(L4, L2, f'{self.h}*', 5, 'right', 'out')

        # Размер d
        if self.d > 0:
            drawer.dimension(L7, R7, f'⌀{self.d}*', -10 - self.s / self.scale)
            # drawer.dimension_diameter(L7, R7, f'{self.d}*', -10 - self.s / self.scale)

        # Размер H
        h = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R8, H0)
        drawer.stroke()
        drawer.dimension(H0, R2, f'{h}±10', -10, 'center', 'in')

        # Размер r
        if self.r > 0:
            drawer.radius_dimension(AL, self.r / self.scale, f'r{self.r}', alpha / 4, offset=10)

        # Размер alpha
        a1 = math.pi / 2 + self.alpha / 2
        a2 = math.pi / 2 - self.alpha / 2
        drawer.dimension_angle(
            A0,
            7 + (self.d / 2) / math.sin(self.alpha / 2) / self.scale,
            a1,
            a2,
            f'{round(math.degrees(self.alpha))}°'
        )
        drawer.stroke()
        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()

    def check_D(self):
        if self.alpha == math.pi / 3:
            alpha = '60'
        elif self.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if str(self.D) in CONE_VALUES[alpha].keys():
            return True
        values = ''.join(list(CONE_VALUES[alpha].keys()))
        my_logger.info(f'''Ошибка в D. Допустимы значения: {values}.''')
        return False

    def check_Dm(self):
        if self.Dm <= 0.75 * self.D:
            return True
        my_logger.info('Ошибка в Dмал. (Dмал ≤ 0.75*Dнр)')
        return False

    def check_r(self):
        if self.alpha == math.pi / 3:
            alpha = '60'
        elif self.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if CONE_VALUES[alpha].get(str(self.D)) is not None:
            if str(self.r) in CONE_VALUES[alpha][str(self.D)].keys():
                return True
            values = ''.join(list(CONE_VALUES[alpha][str(self.D)].keys()))
            my_logger.info(f'''Ошибка в r. Допустимы значения: {values}.''')
            return False

    def check_h(self):
        if self.alpha == math.pi / 3:
            alpha = '60'
        elif self.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if CONE_VALUES[alpha].get(str(self.D)) is not None and CONE_VALUES[alpha][str(self.D)].get(
                str(self.r)) is not None:
            if str(self.h) in CONE_VALUES[alpha][str(self.D)][str(self.r)].keys():
                return True
            values = ''.join(list(CONE_VALUES[alpha][str(self.D)][str(self.r)].keys()))
            my_logger.info(f'''Ошибка в h. Допустимы значения: {values}.''')
            return False

    def check_s(self):
        if self.alpha == math.pi / 3:
            alpha = '60'
        elif self.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if CONE_VALUES[alpha].get(str(self.D)) is not None and CONE_VALUES[alpha][str(self.D)].get(
                str(self.r)) is not None and CONE_VALUES[alpha][str(self.D)][str(self.r)].get(str(self.h)) is not None:
            if str(self.s) in CONE_VALUES[alpha][str(self.D)][str(self.r)][str(self.h)]:
                return True
            values = ''.join(list(CONE_VALUES[alpha][str(self.D)][str(self.r)][str(self.h)]))
            my_logger.info(f'''Ошибка в h. Допустимы значения: {values}.''')
            return False

    def check_values(self):
        b_value = {
            'D': self.check_D(),
            'Dm': self.check_Dm(),
            'R': True,
            'r': self.check_r(),
            's': self.check_s(),
            'h': self.check_h()
        }
        return b_value
