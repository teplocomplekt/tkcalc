import dataclasses
import math
from abc import abstractmethod

from renderer.utils import LineWidth, Color
from utils.enums import ItemFormEnum, ItemSteelEnum
from utils.settings import Q, DEFAULT_WIDTH, A4_PORTRAIT_STAMP, DEFAULT_HIGHT

from utils.settings import VENDOR_NAME


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
    chamfer: bool
    chamfer_value: int
    cut: bool
    weld: bool
    defects: bool
    ultrasonic: bool


class AbstractItem:
    def __init__(self, data: ItemInputDataDTO):
        self.data = data
        self.c2 = 0
        self.c3 = 1

    @property
    def scale(self):
        if self.data.D < DEFAULT_WIDTH:
            scale_x = 1
        else:
            scale_x = self.data.D // DEFAULT_WIDTH
            if self.data.D % DEFAULT_WIDTH > DEFAULT_WIDTH / 2:
                scale_x += 0.5

        if self.get_total_height < DEFAULT_HIGHT:
            scale_y = 1
        else:
            scale_y = self.get_total_height // DEFAULT_HIGHT
            if self.get_total_height % DEFAULT_HIGHT > DEFAULT_HIGHT / 2:
                scale_y += 0.5

        return max(scale_x,scale_y)

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
    def draw(self, drawer):
        raise NotImplementedError()

    def draw_stamp(self, drawer):
        drawer.set_line_style(LineWidth.MEDIUM, Color.BLACK)
        paths = A4_PORTRAIT_STAMP['paths']['medium']
        for path in paths:
            drawer.poly_line(path)

        drawer.stroke()

        drawer.set_line_style(LineWidth.THIN, Color.BLACK)
        paths = A4_PORTRAIT_STAMP['paths']['thin']
        for path in paths:
            drawer.poly_line(path)
        drawer.stroke()

        static_text = A4_PORTRAIT_STAMP['static_text']
        for text in static_text:
            drawer.text(text['title'], text['size'], text['coordinates'])

        static_text_title = A4_PORTRAIT_STAMP['static_text_title']
        for text in static_text_title:
            drawer.text(text['title'], text['size'], text['coordinates'])

        static_text_90 = A4_PORTRAIT_STAMP['static_text_90']
        for text in static_text_90:
            drawer.text(text['title'], text['size'], text['coordinates'], angle=-math.pi / 2)

        # Масса
        drawer.text(f'{math.ceil(self.get_total_weight)}', 7, (177.5, 29.966679), align='center')
        # Масштаб
        drawer.text(f'1:{self.scale}', 7, (195, 29.966679), align='center')

        title = f'{self.title}'
        drawer.text(title, 10, (145, 48.953348), align='center')
        drawer.text(title, 7, (55, 287.5), align='center', angle=math.pi, scale=0.87)
        drawer.text(f'Днище', 15, (120, 28.466675), align='center')
        drawer.text(f'Сталь {self.data.item_steel}', 10, (120, 8.953346), align='center')
        drawer.text(f'{VENDOR_NAME}', 10, (180 - 5 / 4, 8.953346), align='center', scale=0.87)

        additional: list[str] = self.get_default_additional()

        for i, text in enumerate(additional):
            drawer.text(f'{i + 1}. {text}', 7, (25, 60 + (len(additional) - i) * 7), align='left')

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
        c3 = self.data.s * 0.1
        # Суммарная прибавка к толщине стенки обечайки [мм]
        c = c1 + c2 + c3
        return c

    @property
    def _title_template(self):
        raise NotImplementedError()

    @abstractmethod
    def check_values(self):
        raise NotImplementedError()


    def get_default_additional(self) -> list[str]:
        additional: list[str] = []

        additional.append(f'Отклонения согласно ГОСТ 34347-2017')
        additional.append(f'Допускаемое внутренне давление {self.get_total_pressure:.6f} [МПа]')

        if self.data.chamfer:
            additional.append(f'''С фаской {self.data.chamfer_value} мм.''')
        else:
            additional.append('Без фаски.')
        if self.data.cut:
            additional.append('Торцовка/Подрезка.')

        if self.data.weld:
            additional.append('Заварка технологического отверстия.')
        else:
            additional.append('Без заварки технологического отверстия.')

        if self.data.defects:
            additional.append('Дефектоскопия.')

        if self.data.ultrasonic:
            additional.append('УЗК сварных швов.')

        additional.append('Без Термообработки.')

        additional.append('* - размеры для справок.')

        return additional
