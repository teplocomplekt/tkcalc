from abc import abstractmethod
from utils.enums import ItemFormEnum


class AbstractItem:
    @abstractmethod
    def draw(self):
        raise NotImplementedError()


class ThorSphericalItem(AbstractItem):
    def draw(self):
        ...


class SphericalItem(AbstractItem):
    def draw(self):
        ...


class FlatItem(AbstractItem):
    def draw(self):
        ...


class ConeItem(AbstractItem):
    def draw(self):
        ...


class ItemFactory:

    @staticmethod
    def build_item(item_type:ItemFormEnum):
        print(item_type)
        try:
            if item_type == ItemFormEnum.THORSPHERICAL:
                return ThorSphericalItem()
            elif item_type == ItemFormEnum.SPHERICAL:
                return SphericalItem()
            elif item_type == ItemFormEnum.FLAT:
                return FlatItem()
            elif item_type == ItemFormEnum.CONE:
                return ConeItem()
            raise AssertionError("Item type is not valid.")
        except AssertionError as e:
            print(e)
