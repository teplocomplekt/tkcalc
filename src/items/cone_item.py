import logging
import math

from items.abstract_item import AbstractItem
from renderer.utils import LineWidth, Color
from utils.settings import CENTER_POINT
from utils.settings import CONE_VALUES

my_logger = logging.getLogger('my_logger')


class ConeItem(AbstractItem):

    @property
    def get_total_height(self):
        r = self.data.r + self.data.s
        result = self.data.h
        result += r * math.sin(self.data.alpha / 2)
        result += ((self.data.D / 2 - r) + r * math.cos(self.data.alpha / 2) - self.data.Dm / 2) / math.tan(
            self.data.alpha / 2)
        return result

    @property
    def get_total_diameter(self):
        mean_D = self.data.D - self.data.s
        mean_r = self.data.r + self.data.s / 2
        if self.data.alpha == math.pi / 3:
            L = 2 * self.data.h + 1.92 * mean_D + 1.05 * mean_r
            return L
        if self.data.alpha == math.pi / 2:
            L = 2 * self.data.h + 1.289 * mean_D + 1.57 * mean_r
            return L
        my_logger.info('Формула расчета диаметра не применима')
        return 0

    @property
    def get_total_weight(self):
        if self.data.alpha == math.pi / 3:
            b = 180
            mean_d = self.data.d + 0.86 * self.data.s
            L1 = 2 * mean_d
        elif self.data.alpha == math.pi / 2:
            b = 254.31
            mean_d = self.data.d + 0.71 * self.data.s
            L1 = 1.414 * mean_d
        else:
            my_logger.info('Формула расчета веса не применима')
            return 0
        area = 0.785 * (pow(self.get_total_diameter, 2) - pow(L1, 2)) * b / 360
        weight = area * self.data.s * self._density
        return weight

    @property
    def get_total_pressure(self):
        # Согласно ГОСТ 34233.2-2017 Сосуды и аппараты. Нормы и методы расчета на прочность.

        # Применимость:
        # 0.001 ≤ s * cos(α) / D ≤ 0.050 && a > 70*
        if not (0.001 <= self.data.s * math.cos(self.data.alpha) /
                self._id <= 0.050) and self.data.alpha <= math.radians(70):
            my_logger.info('Формула расчета давления не применима (0.001 ≤ s * cos(α) / D ≤ 0.050)')

        # Допускаемое внутреннее избыточное давление [МПа]
        # [p] = 2 * [σ] * φр * (s - c) / (Dκ / cos(α) + (s - c))
        pressure = 2 * self._get_q * self._get_f * (self.data.s - self._get_c) / (
                self._id / math.cos(self.data.alpha / 2) + (self.data.s - self._get_c))
        return pressure

    @property
    def get_k(self):
        sp = (self.data.p * self._id / (2 * self._get_q * self._get_f - self.data.p)) * 1 / math.cos(
            self.data.alpha / 2)
        k = self.data.s / (sp + self._get_c)
        return k

    def draw(self, drawer):
        alpha = self.data.alpha
        drawer.context.save()
        # Смещаем начало координат в центр днища, центр листа
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)

        # Рассчитываем координаты для рисования
        L1 = (-self._id / self.scale / 2, self.data.h / self.scale)
        R1 = (self._id / self.scale / 2, self.data.h / self.scale)

        L2 = ((-self._id / 2 - self.data.s) / self.scale, self.data.h / self.scale)
        R2 = ((self._id / 2 + self.data.s) / self.scale, self.data.h / self.scale)

        L3 = (-self._id / self.scale / 2, 0)
        R3 = (self._id / self.scale / 2, 0)

        L4 = ((-self._id / 2 - self.data.s) / self.scale, 0)
        R4 = ((self._id / 2 + self.data.s) / self.scale, 0)

        AL = ((-self._id / 2 + self.data.r) / self.scale, 0)
        AR = ((self._id / 2 - self.data.r) / self.scale, 0)

        L5 = (AL[0] - (self.data.r / self.scale) * math.cos(alpha / 2),
              AL[1] - (self.data.r / self.scale) * math.sin(alpha / 2))
        R5 = (AR[0] + (self.data.r / self.scale) * math.cos(alpha / 2),
              AR[1] - (self.data.r / self.scale) * math.sin(alpha / 2))

        L6 = (AL[0] - ((self.data.r + self.data.s) / self.scale) * math.cos(alpha / 2),
              AL[1] - ((self.data.r + self.data.s) / self.scale) * math.sin(alpha / 2))
        R6 = (AR[0] + ((self.data.r + self.data.s) / self.scale) * math.cos(alpha / 2),
              AR[1] - ((self.data.r + self.data.s) / self.scale) * math.sin(alpha / 2))

        L7 = (-self.data.Dm / 2 / self.scale, (L5[0] + self.data.Dm / 2 / self.scale) / math.tan(alpha / 2) + L5[1])
        R7 = (self.data.Dm / 2 / self.scale, -(R5[0] - self.data.Dm / 2 / self.scale) / math.tan(alpha / 2) + R5[1])

        L8 = ((-self.data.Dm / 2 - math.cos(alpha / 2) * self.data.s) / self.scale,
              (L5[0] + self.data.Dm / 2 / self.scale) / math.tan(alpha / 2) + L5[1] - math.sin(
                  alpha / 2) * self.data.s / self.scale)
        R8 = ((self.data.Dm / 2 + math.cos(alpha / 2) * self.data.s) / self.scale,
              (L5[0] + self.data.Dm / 2 / self.scale) / math.tan(alpha / 2) + L5[1] - math.sin(
                  alpha / 2) * self.data.s / self.scale)

        H0 = (R2[0], R8[1])
        A0 = (0, L5[0] / math.tan(alpha / 2) + L5[1])

        # # Рисуем левую половинку, внутреннюю часть
        drawer.poly_line([(0, self.data.h / self.scale), L1, L3])
        drawer.arc(*AL, self.data.r / self.scale, math.pi, math.pi + alpha / 2)
        drawer.line(L5, L7)
        drawer.stroke()

        # Рисуем левую половинку
        drawer.poly_line([L1, L2, L4])
        drawer.arc(*AL, (self.data.r + self.data.s) / self.scale, math.pi, math.pi + alpha / 2)
        drawer.line(L6, L8)
        drawer.stroke()

        # # Рисуем правую половинку, внутреннюю часть
        drawer.poly_line([(0, self.data.h / self.scale), R1, R3])
        drawer.arc_negative(*AR, self.data.r / self.scale, 0, -alpha / 2)
        drawer.line(R5, R7)
        drawer.stroke()

        # # Рисуем правую половинку
        drawer.poly_line([R1, R2, R4])
        drawer.arc_negative(*AR, (self.data.r + self.data.s) / self.scale, 0, -alpha / 2)
        drawer.line(R6, R8)
        drawer.stroke()

        # Рисуем тех отверстие
        # if self.data.Dm > 0:
        drawer.line(L8, L7)
        drawer.line(L7, R7)
        drawer.line(R7, R8)

        drawer.line(R8, L8)
        drawer.stroke()

        # Размер D
        drawer.dimension(L2, R2, f'⌀{self.data.D}±2', 10)  # ⌀
        # drawer.dimension_diameter(L1, R1, f'{self.D}±2', 10)  # ⌀

        # Размер s
        drawer.dimension(R1, R2, f'{self.data.s}', 5, 'right', 'out')

        # Размер h
        if self.data.h > 0:
            drawer.dimension(L4, L2, f'{self.data.h}*', 5, 'right', 'out')

        # Размер Dm
        if self.data.Dm > 0:
            drawer.dimension(L7, R7, f'⌀{self.data.Dm}*', -10 - self.data.s / self.scale, align='right')
            # drawer.dimension_diameter(L7, R7, f'{self.d}*', -10 - self.s / self.scale)

        # Размер H
        h = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R8, H0)
        drawer.stroke()
        drawer.dimension(H0, R2, f'{h}±10', -10, 'center', 'in')

        # Размер r
        if self.data.r > 0:
            drawer.radius_dimension(
                AL, self.data.r / self.scale,
                f'r{self.data.r}',
                angle=alpha / 4,
                offset=5 + self.data.s / self.scale
            )

        # Размер alpha
        a1 = math.pi / 2 + self.data.alpha / 2
        a2 = math.pi / 2 - self.data.alpha / 2
        drawer.dimension_angle(
            A0,
            7 + (self.data.Dm / 2) / math.sin(self.data.alpha / 2) / self.scale,
            a1,
            a2,
            f'{round(math.degrees(self.data.alpha))}°'
        )
        drawer.stroke()
        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()

    @property
    def _title_template(self):
        return [
            self._id,
            self.data.Dm,
            self.data.r,
            self.data.h,
            self.data.s
        ]

    def _check_D(self):
        if self.data.alpha == math.pi / 3:
            alpha = '60'
        elif self.data.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if str(self.data.D) in CONE_VALUES[alpha].keys():
            return True
        values = ''.join(list(CONE_VALUES[alpha].keys()))
        my_logger.info(f'''Ошибка в D. Допустимы значения: {values}.''')
        return False

    def _check_Dm(self):
        if self.data.Dm <= 0.75 * self.data.D:
            return True
        my_logger.info('Ошибка в Dмал. (Dмал ≤ 0.75*Dнр)')
        return False

    def _check_r(self):
        if self.data.alpha == math.pi / 3:
            alpha = '60'
        elif self.data.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if CONE_VALUES[alpha].get(str(self.data.D)) is not None:
            if str(self.data.r) in CONE_VALUES[alpha][str(self.data.D)].keys():
                return True
            values = ''.join(list(CONE_VALUES[alpha][str(self.data.D)].keys()))
            my_logger.info(f'''Ошибка в r. Допустимы значения: {values}.''')
            return False

    def _check_h(self):
        if self.data.alpha == math.pi / 3:
            alpha = '60'
        elif self.data.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if CONE_VALUES[alpha].get(str(self.data.D)) is not None and CONE_VALUES[alpha][str(self.data.D)].get(
                str(self.data.r)) is not None:
            if str(self.data.h) in CONE_VALUES[alpha][str(self.data.D)][str(self.data.r)].keys():
                return True
            values = ''.join(list(CONE_VALUES[alpha][str(self.data.D)][str(self.data.r)].keys()))
            my_logger.info(f'''Ошибка в h. Допустимы значения: {values}.''')
            return False

    def _check_s(self):
        if self.data.alpha == math.pi / 3:
            alpha = '60'
        elif self.data.alpha == math.pi / 2:
            alpha = '90'
        else:
            alpha = '90'
        if CONE_VALUES[alpha].get(str(self.data.D)) is not None and CONE_VALUES[alpha][str(self.data.D)].get(
                str(self.data.r)) is not None and CONE_VALUES[alpha][str(self.data.D)][str(self.data.r)].get(
            str(self.data.h)) is not None:
            if str(self.data.s) in CONE_VALUES[alpha][str(self.data.D)][str(self.data.r)][str(self.data.h)]:
                return True
            values = ''.join(list(CONE_VALUES[alpha][str(self.data.D)][str(self.data.r)][str(self.data.h)]))
            my_logger.info(f'''Ошибка в h. Допустимы значения: {values}.''')
            return False

    def check_values(self):
        return {
            'D': self._check_D(),
            # 'Dm': self._check_Dm(),
            'R': True,
            'r': self._check_r(),
            's': self._check_s(),
            'h': self._check_h()
        }
