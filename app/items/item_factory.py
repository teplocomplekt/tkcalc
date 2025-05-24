from items.abstract_item import ItemInputDataDTO
from items.cone_item import ConeItem
from items.flat_item import FlatItem
from items.spherical_item import SphericalItem
from items.thor_spherical_item import ThorSphericalItem
from utils.enums import ItemFormEnum


class ItemFactory:

    # def __init__(self, drawer: Drawer):
    # self.drawer = drawer

    @staticmethod
    def build(data: ItemInputDataDTO):
        try:
            if data.item_form == ItemFormEnum.THORSPHERICAL:
                return ThorSphericalItem(data)
            elif data.item_form == ItemFormEnum.SPHERICAL:
                return SphericalItem(data)
            elif data.item_form == ItemFormEnum.FLAT:
                return FlatItem(data)
            elif data.item_form == ItemFormEnum.CONE:
                return ConeItem(data)
            raise AssertionError("Item type is not valid.")
        except AssertionError as e:
            print(e)

    # def draw_stamp(self):
    #     self.drawer.set_line_style(Drawer.LineWidth.MEDIUM, Drawer.Color.BLACK)
