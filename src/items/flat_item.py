import logging
import math

from items.abstract_item import ItemInputDataDTO
from items.thor_spherical_item import ThorSphericalItem
from renderer.utils import LineWidth, Color
from utils.settings import CENTER_POINT

my_logger = logging.getLogger('my_logger')


class FlatItem(ThorSphericalItem):

    def __init__(self, data: ItemInputDataDTO):
        super().__init__(data=data)
        self.data.R = 10000000

    @property
    def get_total_pressure(self):
        if self.data.s <= self.data.r or self.data.r <= min(self.data.s, 0.1 * self._id):
            my_logger.info('Формула расчета давления не применима max(s;0.25 * s1) ≤ r ≤ min(s1;0.1 * D)')

        pressure = pow((self.data.s - self._get_c) / (self._get_K * self._get_Ko * self._get_Dr),
                       2) * self._get_q * self._get_f
        return pressure

    @property
    def get_k(self):
        sp = self.data.p * self._id / (2 * self._get_q * self._get_f - self.data.p)
        k = self.data.s / (sp + self._get_c)
        return k

    @property
    def get_k1(self):
        s1p = self._get_K * self._get_Ko * self._get_Dr * pow(self.data.p / (self._get_f * self._get_q), 0.5)
        k1 = self.data.s / (s1p + self._get_c)
        return k1

    def draw(self, drawer):
        drawer.context.save()
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        L1 = (-self._id / self.scale / 2, self.data.h / self.scale)
        R1 = (self._id / self.scale / 2, self.data.h / self.scale)
        L2 = ((-self._id / 2 - self.data.s) / self.scale, self.data.h / self.scale)
        R2 = ((self._id / 2 + self.data.s) / self.scale, self.data.h / self.scale)
        L3 = (-self._id / self.scale / 2, 0)
        R3 = (self._id / self.scale / 2, 0)
        L4 = ((-self._id / 2 - self.data.s) / self.scale, 0)
        R4 = ((self._id / 2 + self.data.s) / self.scale, 0)
        L5 = ((-self._id / 2 + self.data.r) / self.scale, -self.data.r / self.scale)
        R5 = ((self._id / 2 - self.data.r) / self.scale, -self.data.r / self.scale)
        L6 = ((-self._id / 2 + self.data.r) / self.scale, (-self.data.r - self.data.s) / self.scale)
        R6 = ((self._id / 2 - self.data.r) / self.scale, (-self.data.r - self.data.s) / self.scale)
        L7 = (-self.data.d / 2 / self.scale, -self.data.r / self.scale)
        R7 = (self.data.d / 2 / self.scale, -self.data.r / self.scale)
        L8 = (-self.data.d / 2 / self.scale, (-self.data.r - self.data.s) / self.scale)
        R8 = (self.data.d / 2 / self.scale, (-self.data.r - self.data.s) / self.scale)
        AL = ((-self._id / 2 + self.data.r) / self.scale, 0)
        AR = ((self._id / 2 - self.data.r) / self.scale, 0)
        H0 = (R2[0], R8[1])

        drawer.poly_line([
            (0, self.data.h / self.scale),
            L1,
            L3])

        # Рисуем левую половинку
        drawer.poly_line([(0, self.data.h / self.scale), L1, L3])
        drawer.arc(*AL, self.data.r / self.scale, math.pi, 3 / 2 * math.pi)
        drawer.line(L5, L7)
        drawer.stroke()

        # # Рисуем левую половинку, внутреннюю часть
        drawer.poly_line([L1, L2, L4])
        drawer.arc(*AL, (self.data.r + self.data.s) / self.scale, math.pi, 3 / 2 * math.pi)
        drawer.line(L6, L8)
        drawer.stroke()

        # # Рисуем правую половинку
        drawer.poly_line([(0, self.data.h / self.scale), R1, R3])
        drawer.arc_negative(*AR, self.data.r / self.scale, 0, -math.pi / 2)
        drawer.line(R5, R7)
        drawer.stroke()

        # # Рисуем правую половинку, внутреннюю часть
        drawer.poly_line([R1, R2, R4])
        drawer.arc_negative(*AR, (self.data.r + self.data.s) / self.scale, 0, -math.pi / 2)
        drawer.line(R6, R8)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.data.d > 0:
            drawer.line(L7, R7)
            drawer.line(R7, R8)
            drawer.line(R8, L8)
            drawer.line(L8, L7)
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
            drawer.dimension(L8, R8, f'⌀{self.data.d}*', -10, 'right', 'out')
            # drawer.dimension_diameter(L8, R8, f'{self.d}*', -10, 'right', 'out')

        # Размер H
        h = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R6, H0)
        drawer.stroke()
        drawer.dimension(H0, R2, f'{h}±10', -10, 'left', 'out')

        # Размер r
        if self.data.r > 0:
            drawer.radius_dimension(
                AL,
                self.data.r / self.scale,
                f'r{self.data.r}',
                math.pi / 4,
                offset=5 + self.data.s / self.scale
            )

        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()

    @property
    def _get_K(self):
        K = 0.35
        return K

    @property
    def _get_Ko(self):
        Ko = 1
        return Ko

    @property
    def _get_Dr(self):
        return self._id - self.data.r * 2

    @property
    def _get_c(self):
        # Прибавка на коррозию [мм]
        c1 = self.data.c1
        # Компенсация минусового допуска [мм]
        c2 = self.c2
        # Технологическая прибавка [мм]
        c3 = self.data.s * 0.1
        # Суммарная прибавка к толщине стенки обечайки [мм]
        c = c1 + c2 + c3
        return c

    @property
    def _title_template(self):
        return [
            self._id,
            self.data.r,
            self.data.h,
            self.data.s
        ]
