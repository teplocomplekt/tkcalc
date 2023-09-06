import logging
import math
import re

from tkinter import ttk
from interface.widgets.ItemSteelWidget import ItemSteelWidget
from interface.widgets.ItemFormWidget import ItemFormWidget
from utils.settings import *
from utils.enums import ItemFormEnum, ItemSteelEnum, ItemHoleWeldEnum
from items.cone_item import ConeItem
from items.flat_item import FlatItem
from items.spherical_item import SphericalItem
from items.thor_spherical_item import ThorSphericalItem
from utils.logger import MyHandlerText
from render.drawer import Drawer
from render.render import Render
from utils.settings import GRID_POSITION, PAD

my_logger = logging.getLogger('my_logger')


class App(tk.Tk):

    def create_item_steel_frame(self):
        parent = ttk.LabelFrame(text='Сталь')
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        for index, item in enumerate(ItemSteelEnum):
            btn = ttk.Radiobutton(
                parent,
                text=item,
                value=item,
                variable=self.item_steel
            )
            btn.grid(
                row=index // 2,
                column=1 if index % 2 > 0 else 0,
                **PAD,
                sticky=tk.NW
            )
        return parent

    def chamfer_callback(self):
        state = self.additional_info_chamfer.get()
        if state:
            self.additional_info_cut.set(value=True)
            self.btn_cut.config(state=tk.DISABLED)
        else:
            self.additional_info_cut.set(value=False)
            self.btn_cut.config(state=tk.NORMAL)

    def create_item_additional_info_chamfer(self, parent):
        btn = ttk.Checkbutton(parent, text='Фаска', variable=self.additional_info_chamfer,
                              command=self.chamfer_callback)
        btn.grid(row=0, column=0, **PAD, sticky=tk.NW)

        entry = ttk.Entry(parent, textvariable=self.additional_info_chamfer_value, width='4')
        entry.grid(row=0, column=1, **PAD, sticky=tk.NW)

        label = ttk.Label(parent, text='градусов')
        label.grid(row=0, column=2, **PAD, sticky=tk.NW)

    def create_item_additional_info_cut(self, parent):
        self.btn_cut = ttk.Checkbutton(parent, text='Подрезка/Торцовка', variable=self.additional_info_cut)
        self.btn_cut.grid(row=0, column=0, **PAD, sticky=tk.NW)

    def create_item_additional_info_defects_insp(self, parent):
        btn = ttk.Checkbutton(parent, text='Дефектоскопия', variable=self.additional_info_defects_insp)
        btn.grid(row=0, column=0, **PAD, sticky=tk.NW)

    def create_item_additional_info_ultrasonic_insp(self, parent):
        btn = ttk.Checkbutton(parent, text='УЗК', variable=self.additional_info_ultrasonic_insp)
        btn.grid(row=0, column=0, **PAD, sticky=tk.NW)

    def create_item_additional_info_hole_weld(self, root):
        parent = ttk.LabelFrame(root, text='Технологическое отверстие')

        btn_weld = ttk.Radiobutton(
            parent,
            text=ItemHoleWeldEnum.WELD,
            value=ItemHoleWeldEnum.WELD,
            variable=self.additional_info_hole_weld
        )
        btn_weld.grid(row=0, column=0, sticky=tk.NW, **PAD, columnspan=3)

        btn_21 = ttk.Radiobutton(
            parent,
            text=ItemHoleWeldEnum.HOLE_21,
            value=ItemHoleWeldEnum.HOLE_21,
            variable=self.additional_info_hole_weld
        )
        btn_21.grid(row=1, column=0, sticky=tk.NW, **PAD, columnspan=3)

        btn_41 = ttk.Radiobutton(
            parent,
            text=ItemHoleWeldEnum.HOLE_41,
            value=ItemHoleWeldEnum.HOLE_41,
            variable=self.additional_info_hole_weld
        )
        btn_41.grid(row=2, column=0, sticky=tk.NW, **PAD, columnspan=3)

        btn_custom = ttk.Radiobutton(
            parent,
            text=ItemHoleWeldEnum.CUSTOM,
            value=ItemHoleWeldEnum.CUSTOM,
            variable=self.additional_info_hole_weld
        )
        btn_custom.grid(row=3, column=0, sticky=tk.NW, **PAD)

        entry_d = ttk.Entry(parent, textvariable=self.d, width='4')
        entry_d.grid(row=3, column=1, sticky=tk.NW, **PAD)

        label_d = ttk.Label(parent, text='мм')
        label_d.grid(row=3, column=2, sticky=tk.NW, **PAD)

        return parent

    def create_item_additional_info(self, root):
        parent = ttk.LabelFrame(root, text='Дополнительные услуги')
        parent.grid_columnconfigure(0, weight=1)

        frame_additional_info_chamfer = ttk.Frame(parent)
        frame_additional_info_chamfer.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        frame_additional_info_cut = ttk.Frame(parent)
        frame_additional_info_cut.grid(row=1, column=0, **PAD, sticky=tk.NSEW)

        frame_additional_info_defects_insp = ttk.Frame(parent)
        frame_additional_info_defects_insp.grid(row=2, column=0, **PAD, sticky=tk.NSEW)

        frame_additional_info_ultrasonic_insp = ttk.Frame(parent)
        frame_additional_info_ultrasonic_insp.grid(row=3, column=0, **PAD, sticky=tk.NSEW)

        self.create_item_additional_info_chamfer(frame_additional_info_chamfer)
        self.create_item_additional_info_cut(frame_additional_info_cut)
        self.create_item_additional_info_defects_insp(frame_additional_info_defects_insp)
        self.create_item_additional_info_ultrasonic_insp(frame_additional_info_ultrasonic_insp)

        return parent

    def disableChildren(self, parent):
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            if wtype not in ('Frame', 'Labelframe', 'TFrame', 'TLabelframe'):
                child.configure(state='disable')
            else:
                self.disableChildren(child)

    def enableChildren(self, parent):
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            if wtype not in ('Frame', 'Labelframe', 'TFrame', 'TLabelframe'):
                child.configure(state='normal')
            else:
                self.enableChildren(child)

    def input_alpha_item(self, root):
        ttk.Label(root, text='Угол α °').grid(GRID_POSITION | {
            'row': 0,
            'column': 0
        })

        parent = ttk.Frame(root)
        parent.grid(
            # GRID_POSITION |
            {
                'row': 0,
                'column': 1
            })

        for index, item in enumerate([60, 90]):
            btn = ttk.Radiobutton(
                parent,
                text=item,
                value=item,
                variable=self.alpha,
            )
            btn.grid(
                # GRID_POSITION |
                {
                    'row': 0,
                    'column': index,
                    # **PAD,
                    'sticky': tk.NW
                }
            )

    def input_dm_item(self, root):

        ttk.Label(root, text='Dмал').grid(
            GRID_POSITION |
            {
                'row': 1,
                'column': 0
            })

        self.entry_Dm = tk.Entry(root, textvariable=self.Dm, width='8')
        self.entry_Dm.grid(
            GRID_POSITION |
            {
                'row': 1,
                'column': 1
            })

    def create_input_cone_frame(self, root):
        parent = ttk.LabelFrame(root, text='Коническое днище')
        self.input_alpha_item(parent)
        self.input_dm_item(parent)
        return parent

    def create_item_input_data(self, root):

        parent = ttk.Frame(root)
        parent.grid_columnconfigure(1, weight=1)

        label_D = ttk.Label(parent, text='Dнр')
        label_D.grid(GRID_POSITION | {'row': 0, 'column': 0})
        self.entry_D = tk.Entry(parent, textvariable=self.D, width='8')
        self.entry_D.grid(row=0, column=1, **PAD, sticky=tk.NSEW)

        label_R = ttk.Label(parent, text='R')
        label_R.grid(GRID_POSITION | {'row': 2, 'column': 0})
        self.entry_R = tk.Entry(parent, textvariable=self.R, width='8')
        self.entry_R.grid(row=2, column=1, **PAD, sticky=tk.NSEW)

        label_r = ttk.Label(parent, text='r')
        label_r.grid(GRID_POSITION | {'row': 3, 'column': 0})
        self.entry_r = tk.Entry(parent, textvariable=self.r, width='8')
        self.entry_r.grid(row=3, column=1, **PAD, sticky=tk.NSEW)

        label_h = ttk.Label(parent, text='h')
        label_h.grid(GRID_POSITION | {'row': 4, 'column': 0})
        self.entry_h = tk.Entry(parent, textvariable=self.h, width='8')
        self.entry_h.grid(row=4, column=1, **PAD, sticky=tk.NSEW)

        label_s = ttk.Label(parent, text='s')
        label_s.grid(GRID_POSITION | {'row': 5, 'column': 0})
        self.entry_s = tk.Entry(parent, textvariable=self.s, width='8')
        self.entry_s.grid(row=5, column=1, **PAD, sticky=tk.NSEW)

        label_p = ttk.Label(parent, text='p')
        label_p.grid(GRID_POSITION | {'row': 6, 'column': 0})
        self.entry_p = tk.Entry(parent, textvariable=self.p, width='8')
        self.entry_p.grid(row=6, column=1, **PAD, sticky=tk.NSEW)

        label_c1 = ttk.Label(parent, text='c1')
        label_c1.grid(GRID_POSITION | {'row': 7, 'column': 0})
        self.entry_c1 = tk.Entry(parent, textvariable=self.c1, width='8')
        self.entry_c1.grid(row=7, column=1, **PAD, sticky=tk.NSEW)

        return parent

    def create_buttons(self, root):
        parent = ttk.Frame(root)
        parent.grid_columnconfigure(0, weight=1)
        button_auto = ttk.Button(parent, text='Рассчитать', command=self.auto_calc_callback)
        button_auto.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        button_manual = ttk.Button(parent, text='Рассчитать вручную', command=self.manual_calc_callback)
        button_manual.grid(row=1, column=0, **PAD, sticky=tk.NSEW)

        button_pdf = ttk.Button(parent, text='Сохранить PDF', command=self.save_pdf_callback)
        button_pdf.grid(row=2, column=0, **PAD, sticky=tk.NSEW)

        return parent

    def create_calc(self, parent1, parent2):
        label_total_height = ttk.Label(parent1, text='Общая высота днища')
        label_total_height.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        label_calc_total_height = ttk.Label(parent2, textvariable=self.calc_total_height)
        label_calc_total_height.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        label_total_diameter = ttk.Label(parent1, text='Диаметр заготовки')
        label_total_diameter.grid(row=1, column=0, **PAD, sticky=tk.NSEW)

        label_calc_total_diameter = ttk.Label(parent2, textvariable=self.calc_total_diameter)
        label_calc_total_diameter.grid(row=1, column=0, **PAD, sticky=tk.NSEW)

        label_total_weight = ttk.Label(parent1, text='Масса готового днища')
        label_total_weight.grid(row=2, column=0, **PAD, sticky=tk.NSEW)

        label_calc_total_wieght = ttk.Label(parent2, textvariable=self.calc_total_weight)
        label_calc_total_wieght.grid(row=2, column=0, **PAD, sticky=tk.NSEW)

        label_total_pressure = ttk.Label(parent1, text='Допускаемое внутренне давление')
        label_total_pressure.grid(row=3, column=0, **PAD, sticky=tk.NSEW)

        label_calc_total_pressure = ttk.Label(parent2, textvariable=self.calc_total_pressure)
        label_calc_total_pressure.grid(row=3, column=0, **PAD, sticky=tk.NSEW)

        label_total_k = ttk.Label(parent1, text='Запас прочности')
        label_total_k.grid(row=4, column=0, **PAD, sticky=tk.NSEW)

        self.label_calc_total_k = ttk.Label(parent2, textvariable=self.calc_total_k)
        self.label_calc_total_k.grid(row=4, column=0, **PAD, sticky=tk.NSEW)

        self.label_total_k1 = ttk.Label(parent1, text='Запас прочности крышки', state=tk.DISABLED)
        self.label_total_k1.grid(row=5, column=0, **PAD, sticky=tk.NSEW)

        self.label_calc_total_k1 = ttk.Label(parent2, textvariable=self.calc_total_k1, state=tk.DISABLED)
        self.label_calc_total_k1.grid(row=5, column=0, **PAD, sticky=tk.NSEW)

    def create_logger(self):
        parent = ttk.Frame()
        self.logtext = tk.Text(parent, state="disabled", width=50, height=5)
        self.logtext.pack()

        stderrHandler = logging.StreamHandler()  # no arguments => stderr
        my_logger.addHandler(stderrHandler)
        guiHandler = MyHandlerText(self.logtext)
        my_logger.addHandler(guiHandler)
        my_logger.setLevel(logging.INFO)

        return parent

    def clear_log(self):
        self.logtext.configure(state='normal')
        self.logtext.delete("1.0", tk.END)
        self.logtext.configure(state='disabled')

    def init_callback(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # устанавливаем заголовок окна
        self.title(APP_TITLE)
        # Запрещаем fullscreen
        self.resizable(False, False)

        # Иконка
        self.wm_iconphoto(False, tk.PhotoImage(file=BASE_DIR / 'icon.png'))

    def __init__(self=None):
        super(App, self).__init__()

        frame_logger = self.create_logger()

        self.init_callback()

        # Переменные на форме
        self.item_form = tk.StringVar(value=ItemFormEnum.default())
        self.item_steel = tk.StringVar(value=ItemSteelEnum.default())

        # Входные данные
        self.D = tk.StringVar(value='1000')  # Диаметр
        self.Dm = tk.StringVar(value='500')  # Диаметр малый (конический)
        self.R = tk.StringVar(value='730')  # Радиус большой
        self.r = tk.StringVar(value='100')  # Радиус малый
        self.s = tk.StringVar(value='20')  # Толщина
        self.h = tk.StringVar(value='100')  # Высота борта
        self.d = tk.StringVar(value='100')  # Диаметр тех. отверстия
        self.p = tk.StringVar(value='1')  # Максимальное давление
        self.c1 = tk.StringVar(value='2.0')  # Максимальное давление

        self.alpha = tk.IntVar(value=90)  # угол для конуса
        # Доп услуги
        self.additional_info_chamfer = tk.BooleanVar()
        self.additional_info_chamfer_value = tk.StringVar(value=45)
        self.additional_info_cut = tk.BooleanVar()
        self.additional_info_defects_insp = tk.BooleanVar()
        self.additional_info_ultrasonic_insp = tk.BooleanVar()
        self.additional_info_hole_weld = tk.StringVar(value=ItemHoleWeldEnum.default())

        # Расчет
        self.calc_total_height = tk.StringVar()
        self.calc_total_diameter = tk.StringVar()
        self.calc_total_weight = tk.StringVar()
        self.calc_total_pressure = tk.StringVar()
        self.calc_total_k = tk.StringVar()
        self.calc_total_k1 = tk.StringVar()

        ItemFormWidget(
            text='Форма днища',
            variable=self.item_form,
            command=self.form_select_callback
        ).grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        ItemSteelWidget(
            text='Сталь',
            variable=self.item_steel,
        ).grid(row=0, column=1, **PAD, sticky=tk.NSEW)

        left_frame = ttk.Frame()
        left_frame.grid_columnconfigure(0, weight=1)

        frame_additional_info = self.create_item_additional_info(left_frame)
        frame_additional_info.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        frame_additional_info_hole_weld = self.create_item_additional_info_hole_weld(left_frame)
        frame_additional_info_hole_weld.grid(row=1, column=0, **PAD, sticky=tk.NSEW, )

        self.input_cone_frame = self.create_input_cone_frame(left_frame)
        self.input_cone_frame.grid(row=2, column=0, **PAD, sticky=tk.NSEW)

        # self.disableChildren(self.input_alpha_frame)

        left_frame.grid(row=1, column=0, **PAD, sticky=tk.NSEW)

        frame_calc_label = ttk.Frame(text=None)
        frame_calc_label.grid(row=2, column=0, **PAD, sticky=tk.NSEW)

        frame_logger.grid(row=3, column=0, **PAD, sticky=tk.NSEW, columnspan=2)

        # ==========

        right_frame = ttk.Frame()
        right_frame.grid_columnconfigure(0, weight=1)

        frame_input = self.create_item_input_data(right_frame)
        frame_input.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        frame_buttons = self.create_buttons(right_frame)
        frame_buttons.grid(row=1, column=0, **PAD, sticky=tk.NSEW)

        right_frame.grid(row=1, column=1, **PAD, sticky=tk.NSEW)

        frame_calc_value = ttk.Frame(text=None)
        frame_calc_value.grid(row=2, column=1, **PAD, sticky=tk.NSEW)

        self.create_calc(frame_calc_label, frame_calc_value)
        self.form_select_callback()

    def is_not_empty(self, value, title):
        if not value:
            my_logger.info(f'Поле {title} должно быть заполнено!')
            self.mark_field(title)
            return False
        else:
            return True

    def is_int(self, value, title):
        result = re.match("^\d{0,11}$", value)
        if not result:
            my_logger.info(f'Поле {title} должно быть числом!')
            self.mark_field(title)
            return False
        else:
            return True

    def validate(self, value, title):
        if self.is_not_empty(value, title) and self.is_int(value, title):
            return int(value)
        else:
            raise ValueError

        # Getters

    def get_D(self):
        D = self.D.get()
        return self.validate(D, 'D')

    def get_d(self):
        if self.additional_info_hole_weld.get() == ItemHoleWeldEnum.WELD:
            d = '0'
        elif self.additional_info_hole_weld.get() == ItemHoleWeldEnum.HOLE_21:
            d = '21'
        elif self.additional_info_hole_weld.get() == ItemHoleWeldEnum.HOLE_41:
            d = '41'
        else:
            d = self.d.get()
        return self.validate(d, 'd')

    def get_R(self):
        R = self.R.get()
        return self.validate(R, 'R')

    def get_r(self):
        r = self.r.get()
        return self.validate(r, 'r')

    def get_s(self):
        s = self.s.get()
        return self.validate(s, 's')

    def get_h(self):
        h = self.h.get()
        return self.validate(h, 'h')

    def get_p(self):
        p = self.p.get()
        return self.validate(p, 'p')

    def get_weld(self):
        return self.additional_info_hole_weld.get() == ItemHoleWeldEnum.WELD

    def get_chamfer_value(self):
        if self.additional_info_chamfer.get():
            chamfer_value = self.additional_info_chamfer_value.get()
            return self.validate(chamfer_value, 'chamfer_value')
        else:
            return 0

    def get_alpha(self):
        a = self.alpha.get()
        return a

    def get_Dm(self):
        Dm = self.Dm.get()
        return self.validate(Dm, 'D.мал')

    def get_c1(self):
        c1 = self.Dm.get()
        return c1

    def init_args(self):
        try:
            D = self.get_D()
            Dm = self.get_Dm()
            d = self.get_d()
            R = self.get_R()
            r = self.get_r()
            s = self.get_s()
            h = self.get_h()
            p = self.get_p()
            c1 = self.get_c1()
            form = self.item_form.get()
            steel = self.item_steel.get()
            weld = self.get_weld()
            chamfer = self.additional_info_chamfer.get()
            chamfer_value = self.get_chamfer_value()
            cut = self.additional_info_cut.get()
            defects_insp = self.additional_info_defects_insp.get()
            ultrasonic_insp = self.additional_info_ultrasonic_insp.get()
            alpha = self.get_alpha()


            return {
                'D': D, 'Dm': Dm, 'd': d, 'R': R, 'r': r, 's': s, 'h': h, 'p': p, 'c1': c1, 'form': form,
                'steel': steel, 'weld': weld,
                'chamfer': chamfer, 'chamfer_value': chamfer_value, 'cut': cut,
                'defects_insp': defects_insp,
                'ultrasonic_insp': ultrasonic_insp,
                'alpha': alpha,

            }

        except Exception as e:
            my_logger.info(f'Ошибка: {e}')

    def clear_calc_values(self):
        self.calc_total_height.set('')
        self.calc_total_diameter.set('')
        self.calc_total_weight.set('')
        self.calc_total_pressure.set('')
        self.calc_total_k.set('')
        self.calc_total_k1.set('')

    def set_calc_values(self, item):
        try:
            self.calc_total_height.set('%s мм' % round(item.get_total_height))
            self.calc_total_diameter.set('%s мм' % round(item.get_total_diameter))
            self.calc_total_weight.set('%s кг' % math.ceil(item.get_total_weight))
            self.calc_total_pressure.set('%s МПа' % round(item.get_total_pressure, 6))
            k = item.get_k

            self.calc_total_k.set(round(k, 2))

            if k >= 1:
                self.label_calc_total_k.configure(foreground='green')
            else:
                self.label_calc_total_k.configure(foreground='red')
                my_logger.info('Прочность не обеспечена.')

            if self.item_form.get() == ItemFormEnum.FLAT:
                k1 = item.get_k1
                self.calc_total_k1.set(round(k1, 2))
                if k1 >= 1:
                    self.label_calc_total_k1.configure(foreground='green')
                else:
                    self.label_calc_total_k1.configure(foreground='red')
                    my_logger.info('Прочность крышки не обеспечена.')

        except Exception as e:
            my_logger.info(f'Не удалось посчитать: {e}')

    def mark_entries_color(self, marks=None):
        if marks is None:
            marks = {
                'D': True,
                'R': True,
                'r': True,
                's': True,
                'h': True,
            }
        for mark, value in marks.items():
            entry = getattr(self, f'entry_{mark}')
            if value:
                entry.configure(background="white")
            else:
                entry.configure(background="pink")

    def mark_entries_state(self, marks=None):
        if marks is None:
            marks = {
                'D': True,
                'R': True,
                'r': True,
                's': True,
                'h': True,
            }
        for mark, value in marks.items():
            entry = getattr(self, f'entry_{mark}')
            if value:
                entry.configure(state=tk.NORMAL)
            else:
                entry.configure(state=tk.DISABLED)

    def form_select_callback(self):
        form = self.item_form.get()
        if form == ItemFormEnum.THORSPHERICAL:
            marks = {
                'D': True,
                'R': True,
                'r': True,
                's': True,
                'h': True,
            }
            self.mark_entries_state(marks=marks)
            self.disableChildren(self.input_cone_frame)
            self.label_total_k1.configure(state=tk.DISABLED)
            self.label_calc_total_k1.configure(state=tk.DISABLED)
        elif form == ItemFormEnum.SPHERICAL:
            marks = {
                'D': True,
                'R': True,
                'r': False,
                's': True,
                'h': False,
            }
            # self.r.set('0')
            # self.h.set('0')
            self.mark_entries_state(marks=marks)
            self.disableChildren(self.input_cone_frame)
            self.label_total_k1.configure(state=tk.DISABLED)
            self.label_calc_total_k1.configure(state=tk.DISABLED)
        elif form == ItemFormEnum.FLAT:
            marks = {
                'D': True,
                'R': False,
                'r': True,
                's': True,
                'h': True,
            }
            # self.R.set('1000000')
            self.mark_entries_state(marks=marks)
            self.disableChildren(self.input_cone_frame)
            self.label_total_k1.configure(state=tk.NORMAL)
            self.label_calc_total_k1.configure(state=tk.NORMAL)

        elif form == ItemFormEnum.CONE:
            marks = {
                'D': True,
                'R': False,
                'r': True,
                's': True,
                'h': True,
            }
            self.mark_entries_state(marks=marks)
            self.enableChildren(self.input_cone_frame)
            self.label_total_k1.configure(state=tk.DISABLED)
            self.label_calc_total_k1.configure(state=tk.DISABLED)

    def get_item(self, **args):
        form = self.item_form.get()
        if form == ItemFormEnum.THORSPHERICAL:
            return ThorSphericalItem(**args)
        elif form == ItemFormEnum.SPHERICAL:
            return SphericalItem(**args)
        elif form == ItemFormEnum.FLAT:
            return FlatItem(**args)
        elif form == ItemFormEnum.CONE:
            return ConeItem(**args)

    def auto_calc_callback(self):
        args = self.init_args()
        self.clear_calc_values()
        item = self.get_item(**args)
        self.clear_log()
        marks = item.check_values()
        self.mark_entries_color(marks)
        if not False in marks.values():
            self.set_calc_values(item)

    def manual_calc_callback(self):
        args = self.init_args()
        self.clear_calc_values()
        item = self.get_item(**args)
        self.clear_log()
        self.set_calc_values(item)

    def save_pdf_callback1(self):
        args = self.init_args()
        self.clear_calc_values()
        item = self.get_item(**args)
        self.clear_log()
        self.set_calc_values(item)

        render = Render.get_render('SVG', '')
        drawer = Drawer(render)
        item.draw_stamp(drawer)
        item.draw(drawer)

        render.save()

    def save_pdf_callback(self):
        args = self.init_args()
        self.clear_calc_values()
        item = self.get_item(**args)
        self.clear_log()
        self.set_calc_values(item)

        try:
            title = item.title
            # render = Render.get_render('SVG')
            render = Render.get_render('PDF', title)
            drawer = Drawer(render)
            item.draw_stamp(drawer)
            item.draw(drawer)

            render.save()
        except Exception as e:
            my_logger.info(f'Не удалось сохранить: {e}')
