import logging
import math
from abc import ABC, abstractmethod

from render.drawer import Drawer, LineWidth, Color

from utils.enums import ItemSteelEnum, ItemFormEnum
from utils.settings import *

my_logger = logging.getLogger('my_logger')


class BaseItem(ABC):
    D = 0
    Dm = 0
    d = 0
    R = 0
    r = 0
    s = 0
    h = 0
    p = 0
    c1 = 0
    item_steel = ItemSteelEnum.default()
    item_form = ItemFormEnum.default()
    weld = False
    chamfer = False
    chamfer_value = 0
    cut = False
    defects_insp = False
    ultrasonic_insp = False
    alpha = math.pi / 2
    _title_template = []

    def __init__(
            self,
            D,
            Dm,
            d,
            R,
            r,
            s,
            h,
            p,
            c1,
            form,
            steel,
            weld,
            chamfer,
            chamfer_value,
            cut,
            defects_insp,
            ultrasonic_insp,
            alpha
    ):
        super().__init__()
        self.D = int(D)
        self.Dm = int(Dm)
        self.d = int(d)
        self.R = int(R)
        self.r = int(r)
        self.s = int(s)
        self.h = int(h)
        self.p = float(p)
        self.c1 = float(c1)
        self.c2 = 0
        self.c3 = 1
        self.item_form = form
        self.item_steel = steel
        self.weld = weld
        self.chamfer = chamfer
        self.chamfer_value = chamfer_value
        self.cut = cut
        self.defects_insp = defects_insp
        self.ultrasonic_insp = ultrasonic_insp
        self.alpha = math.radians(alpha)

    @property
    def title(self):
        H = 5 * math.ceil(self.get_total_height / 5)
        title = '-'.join(map(str, self._title_template))
        return f'{title} H={H}'

    @property
    def _id(self):
        return self.D - self.s - self.s

    @property
    def _get_Q(self):
        Q = {
            ItemSteelEnum.STEEL_BT_1: 143,
            ItemSteelEnum.STEEL_AISI_409: 159,
            ItemSteelEnum.STEEL_AISI_316: 179,
            ItemSteelEnum.STEEL_AISI_321: 179,
            ItemSteelEnum.STEEL_AISI_304: 170,
            ItemSteelEnum.STEEL_09G2C: 195,
            ItemSteelEnum.STEEL_3: 154
        }
        return Q[self.item_steel]

    @property
    def _get_f(self):
        # Коэффициент прочности продольного сварного шва
        f = 1  # Для днищ, изготовленных из одной заготовки, коэффициент φ = 1.
        return f

    @property
    def _get_c(self):
        # Прибавка на коррозию [мм]
        c1 = self.c1
        # Компенсация минусового допуска [мм]
        c2 = self.c2
        # Технологическая прибавка [мм]
        c3 = self.c3
        # Суммарная прибавка к толщине стенки обечайки [мм]
        c = c1 + c2 + c3
        return c

    @property
    def density(self):
        """
        if (name_metal == "Ст3" || "09Г2С") {return density = 0.00000785;}else {return density = 0.00000833;}
        if (name_metal == "BT-1") {return density = 0.000001;}
        """
        density = 0.00000833
        if self.item_steel == ItemSteelEnum.STEEL_3 or self.item_steel == ItemSteelEnum.STEEL_09G2C:
            density = 0.00000785

        if self.item_steel == ItemSteelEnum.STEEL_BT_1:
            density = 0.0000045
        return density

    @property
    def get_total_height(self):
        return 0

    @property
    def get_total_diameter(self):
        return 0

    @property
    def get_total_weight(self):
        return 0

    @property
    def get_total_pressure(self):
        return 0

    @property
    def get_k(self):
        return 0

    @property
    def get_k1(self):
        return 0

    @property
    def scale(self):
        if self.D < DEFAULT_WIDTH:
            scale = 1
            return scale
        scale = self.D // DEFAULT_WIDTH
        if self.D % DEFAULT_WIDTH > DEFAULT_WIDTH / 2:
            scale += 0.5
        return scale

    def draw_stamp(self, drawer: Drawer):
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

        # form = self.item_form.split('/')[0]

        # drawer.text('Разраб.', 5, (20.5, 30.726673))
        # title = f'Чертеж №___ {date.today().strftime("%Y.%m.%d")}'
        title = f'{self.title}'
        drawer.text(title, 10, (145, 48.953348), align='center')
        drawer.text(title, 7, (55, 287.5), align='center', angle=math.pi, scale=0.87)
        drawer.text(f'Днище', 15, (120, 28.466675), align='center')
        drawer.text(f'Сталь {self.item_steel}', 10, (120, 8.953346), align='center')
        drawer.text(f'Теплокомплект', 10, (180 - 5 / 4, 8.953346), align='center', scale=0.87)

        additional = []

        if self.chamfer:
            additional.append(f'''С фаской {self.chamfer_value} мм.''')
        else:
            additional.append('Без фаски.')
        if self.cut:
            additional.append('Торцовка/Подрезка.')

        if self.weld:
            additional.append('Заварка технологического отверстия.')
        else:
            additional.append('Без заварки технологического отверстия.')

        if self.defects_insp:
            additional.append('Дефектоскопия.')

        if self.ultrasonic_insp:
            additional.append('УЗК сварных швов.')

        additional.append('Без Термообработки.')

        additional.append('* - размеры для справок.')

        for i, text in enumerate(additional):
            drawer.text(f'{i + 1}. {text}', 7, (25, 60 + (len(additional) - i) * 7), align='left')

    @abstractmethod
    def draw(self, drawer: Drawer):
        pass

    def _get_optimal(self, value: int, array):
        array = list(map(int, array))

        result = ''

        if value < array[0]:
            result = array[0]
        if value > array[-1]:
            result = array[-1]
        else:
            for i in range(len(array)):
                if array[i] <= value < array[i + 1]:
                    if value == array[i]:
                        result = array[i]
                    else:
                        result = array[i + 1]
        return str(result)

    @abstractmethod
    def check_values(self):
        pass
