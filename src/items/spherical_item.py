import logging
import math

from items.abstract_item import ItemInputDataDTO
from items.thor_spherical_item import ThorSphericalItem
from renderer.utils import LineWidth, Color
from utils.settings import CENTER_POINT

my_logger = logging.getLogger('my_logger')


class SphericalItem(ThorSphericalItem):

    def __init__(self, data: ItemInputDataDTO):
        super().__init__(data=data)
        self.data.r = 0
        self.data.h = 0

    # @property
    # def get_total_height(self):
    #     pass
    #
    # @property
    # def get_total_diameter(self):
    #     pass
    #
    # @property
    # def get_total_weight(self):
    #     pass

    # @property
    # def get_total_pressure(self):
    #     pressure = 2 * (self.data.s - self._get_c) * self._get_f * self._get_q /\
    #                (self._get_R + 0.5 * (self.data.s - self._get_c))
    #     return pressure

    # @property
    # def get_k(self):
    #     pass

    def draw(self, drawer):
        drawer.context.save()
        drawer.context.translate(CENTER_POINT[0], CENTER_POINT[1] + self.get_total_height / 2 / self.scale)
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        L1 = (-self._id / self.scale / 2, 0)
        R1 = (self._id / self.scale / 2, 0)
        L2 = (-(self.data.R + self.data.s) * math.cos(self._angle) / self.scale,
              (self._height_R - (self.data.R + self.data.s) * math.sin(self._angle)) / self.scale)
        R2 = ((self.data.R + self.data.s) * math.cos(self._angle) / self.scale,
              (self._height_R - (self.data.R + self.data.s) * math.sin(self._angle)) / self.scale)
        L3 = (-self.data.d / 2 / self.scale, self._height / self.scale)
        R3 = (self.data.d / 2 / self.scale, self._height / self.scale)
        L4 = (-self.data.d / 2 / self.scale, (self._height - self.data.s) / self.scale)
        R4 = (self.data.d / 2 / self.scale, (self._height - self.data.s) / self.scale)
        H0 = (R1[0], R4[1])
        A0 = (0, self._height_R / self.scale)
        drawer.poly_line([
            (0, 0),
            L1,
            L2])

        # Рисуем левую половинку, внешнюю часть
        drawer.arc(*A0, (self.data.R + self.data.s) / self.scale, math.pi + self._angle, - math.pi / 2 - self._angle1)
        drawer.stroke()
        # Рисуем левую половинку, внутреннюю часть
        drawer.arc(*A0, self.data.R / self.scale, math.pi + self._angle, -math.pi / 2 - self._angle1)
        drawer.stroke()

        # Рисуем правую половинку
        drawer.poly_line([(0, 0), R1, R2])
        # Рисуем правую половинку, внешнюю часть
        drawer.arc_negative(*A0, (self.data.R + self.data.s) / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()
        # Рисуем правую половинку, внутреннюю часть
        drawer.arc_negative(*A0, self.data.R / self.scale, -self._angle, -math.pi / 2 + self._angle1)
        drawer.stroke()

        # Рисуем тех отверстие
        if self.data.d > 0:
            drawer.line(L3, R3)
            drawer.line(R3, R4)
            drawer.line(R4, L4)
            drawer.line(L4, L3)
            drawer.stroke()

        # Размер D
        drawer.dimension(L2, R2, f'⌀{self.data.D}±2', 10)  # ⌀
        # drawer.dimension_diameter(L1, R1, f'{self.D}±2', 10)  # ⌀

        # Размер s
        drawer.dimension_thickness(
            center=A0,
            radius=self.data.R / self.scale,
            thickness=self.data.s / self.scale,
            text=f'{self.data.s}*',
            angle=((math.pi / 2 - self._angle - self._angle1) * 2 / 3 + self._angle),
            offset=5 + self.data.s / self.scale
        )

        # Размер d
        if self.data.d > 0:
            drawer.dimension(L4, R4, f'⌀{self.data.d}*', -10, 'right', 'out')
            # drawer.dimension_diameter(L4, R4, f'{self.d}*', -10, 'right', 'out')

        # Размер H
        H = int(round(self.get_total_height))
        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        drawer.line(R4, H0)
        drawer.stroke()
        drawer.dimension(H0, R1, f'{H}±10', -10, 'center', 'in')

        # Размер R
        drawer.radius_dimension(
            center=A0,
            radius=self.data.R / self.scale,
            text=f'R{self.data.R}',
            # angle=(self._angle / 3 + math.pi / 4 - self._angle1),
            angle=((math.pi / 2 - self._angle - self._angle1) * 1 / 3 + self._angle),
            offset=5
        )

        # смещаем начало координат обратно в левый нижний угол листа
        drawer.context.restore()

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
            self.data.D,
            self.data.R,
            # self.r,
            # self.h,
            self.data.s,
        ]

    def _check_s(self):
        if self.s < self.s or self.s < 40:
            return True
        my_logger.info('Ошибка в s.(3 < s < 40)')
        return False

    def check_values(self):

        return {
            'D': self._check_D(),
            # 'Dm': True,
            'R': self._check_R(),
            'r': True,
            's': self._check_s(),
            'h': True}
