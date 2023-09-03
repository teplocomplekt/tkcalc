from enum import Enum

from utils.settings import *


class ItemFormEnum(str, Enum):
    THORSPHERICAL = 'Эллиптическое/Торосферическое'
    SPHERICAL = 'Сферическое'
    FLAT = 'Плоское'
    CONE = 'Коническое'

    @staticmethod
    def default():
        return ItemFormEnum.THORSPHERICAL


class ItemSteelEnum(str, Enum):
    STEEL_3 = STEEL_3
    STEEL_AISI_409 = 'AiSi 409'
    STEEL_09G2C = '09Г2С'
    STEEL_AISI_304 = 'AiSi 304'
    STEEL_BT_1 = 'ВТ-1'
    STEEL_AISI_321 = 'AiSi 321'
    STEEL_AISI_316 = 'AiSi 316'

    @staticmethod
    def default():
        return ItemSteelEnum.STEEL_3


class ItemHoleWeldEnum(str, Enum):
    WELD = 'Заварить'
    HOLE_21 = '21 мм'
    HOLE_41 = '41 мм'
    CUSTOM = 'Задать'

    @staticmethod
    def default():
        return ItemHoleWeldEnum.HOLE_41


class ItemHEnum(str, Enum):
    H_35 = '* 3,5'
    H_50 = '* 5'
    CUSTOM = 'Задать'

    @staticmethod
    def default():
        return ItemHEnum.H_50
