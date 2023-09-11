from items.abstract_item import ItemInputDataDTO
from items.thor_spherical_item import ThorSphericalItem


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
        ...

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
