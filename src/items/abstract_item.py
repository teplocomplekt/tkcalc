import dataclasses
import math
from abc import abstractmethod

from utils.enums import ItemFormEnum, ItemSteelEnum
from utils.settings import Q, DEFAULT_WIDTH


@dataclasses.dataclass
class ItemInputDataDTO:
    item_form: ItemFormEnum
    item_steel: ItemSteelEnum
    D: int
    d: int
    Dm: int
    alpha: float
    R: int
    r: int
    h: int
    s: int
    p: float
    c1: float


class AbstractItem:
    def __init__(self, data: ItemInputDataDTO):
        self.data = data
        self.c2 = 0
        self.c3 = 1

    @property
    def scale(self):
        if self.data.D < DEFAULT_WIDTH:
            scale = 1
            return scale
        scale = self.data.D // DEFAULT_WIDTH
        if self.data.D % DEFAULT_WIDTH > DEFAULT_WIDTH / 2:
            scale += 0.5
        return scale

    @property
    def get_total_height(self):
        raise NotImplementedError()

    @property
    def get_total_diameter(self):
        raise NotImplementedError()

    @property
    def get_total_weight(self):
        raise NotImplementedError()

    @property
    def get_total_pressure(self):
        raise NotImplementedError()

    @property
    def get_k(self):
        return 0

    @property
    def get_k1(self):
        return 0

    @abstractmethod
    def draw(self):
        raise NotImplementedError()

    @property
    def title(self):
        H = 5 * math.ceil(self.get_total_height / 5)
        title = '-'.join(map(str, self._title_template))
        return f'{title} H={H}'

    @property
    def _id(self):
        return self.data.D - 2 * self.data.s

    @property
    def _density(self):
        density = 0.00000833
        if self.data.item_steel == ItemSteelEnum.STEEL_3 or self.data.item_steel == ItemSteelEnum.STEEL_09G2C:
            density = 0.00000785
        if self.data.item_steel == ItemSteelEnum.STEEL_BT_1:
            density = 0.0000045

        return density

    @property
    def _get_q(self):
        return Q[self.data.item_steel]

    @property
    def _get_f(self):
        # Коэффициент прочности продольного сварного шва
        f = 1  # Для днищ, изготовленных из одной заготовки, коэффициент φ = 1.
        return f

    @property
    def _get_c(self):
        # Прибавка на коррозию [мм]
        c1 = self.data.c1
        # Компенсация минусового допуска [мм]
        c2 = self.c2
        # Технологическая прибавка [мм]
        c3 = self.c3
        # Суммарная прибавка к толщине стенки обечайки [мм]
        c = c1 + c2 + c3
        return c

    @property
    def _title_template(self):
        raise NotImplementedError()
