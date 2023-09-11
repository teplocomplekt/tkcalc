import logging
import math

from items.abstract_item import AbstractItem

my_logger = logging.getLogger('my_logger')

class ConeItem(AbstractItem):



    @property
    def get_total_height(self):
        r = self.data.r + self.data.s
        result = self.data.h
        result += r * math.sin(self.data.alpha / 2)
        result += ((self.data.D / 2 - r) + r * math.cos(self.data.alpha / 2) - self.data.Dm / 2) / math.tan(self.data.alpha / 2)
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
        sp = (self.data.p * self._id / (2 * self._get_q * self._get_f - self.data.p)) * 1 / math.cos(self.data.alpha / 2)
        k = self.data.s / (sp + self._get_c)
        return k

    def draw(self, drawer):
        ...

    @property
    def _title_template(self):
        return [
            self._id,
            self.data.Dm,
            self.data.r,
            self.data.h,
            self.data.s
        ]