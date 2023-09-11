import math

from items.abstract_item import AbstractItem


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

    def draw(self):
        ...

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