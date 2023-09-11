import logging

from items.abstract_item import ItemInputDataDTO
from items.thor_spherical_item import ThorSphericalItem

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
        ...

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
