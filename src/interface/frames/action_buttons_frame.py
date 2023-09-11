import logging
import math
import tkinter
from tkinter import ttk

from items.abstract_item import ItemInputDataDTO
from items.item_factory import ItemFactory
from renderer.drawer import Drawer
from renderer.render import RenderFactory, RenderTypeEnum
from renderer.utils import PaperSize
from utils.enums import ItemFormEnum
from utils.settings import PAD

my_logger = logging.getLogger('my_logger')


class ActionButtonsFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.item = None

        self.grid_columnconfigure(0, weight=1)

        button_auto = ttk.Button(self, text='Рассчитать', command=self.auto_calc_callback)
        button_auto.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        button_manual = ttk.Button(self, text='Рассчитать вручную', command=self.manual_calc_callback)
        button_manual.grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)

        button_pdf = ttk.Button(self, text='Сохранить PDF', command=self.save_pdf_callback)
        button_pdf.grid(row=2, column=0, **PAD, sticky=tkinter.NSEW)

    def auto_calc_callback(self):
        my_logger.info('auto_calc_callback')
        self.manual_calc_callback()

    def manual_calc_callback(self):
        my_logger.info('manual_calc_callback')
        data = ItemInputDataDTO(
            item_form=self.parent.parent.item_form_frame.variable.get(),
            item_steel=self.parent.parent.item_steel_frame.variable.get(),
            D=self.parent.parent.right_frame.input_data_frame.D.get(),
            d=self.parent.parent.left_frame.hole_weld_frame.d.get(),
            Dm=self.parent.parent.left_frame.cone_input_frame.Dm.get(),
            alpha=math.radians(self.parent.parent.left_frame.cone_input_frame.alpha.get()),
            R=self.parent.parent.right_frame.input_data_frame.R.get(),
            r=self.parent.parent.right_frame.input_data_frame.r.get(),
            h=self.parent.parent.right_frame.input_data_frame.h.get(),
            s=self.parent.parent.right_frame.input_data_frame.s.get(),
            p=self.parent.parent.right_frame.input_data_frame.p.get(),
            c1=self.parent.parent.right_frame.input_data_frame.c1.get(),
            chamfer=self.parent.parent.left_frame.additional_info_frame.chamfer.chamfer.get(),
            chamfer_value=self.parent.parent.left_frame.additional_info_frame.chamfer.chamfer_value.get(),
            cut=self.parent.parent.left_frame.additional_info_frame.cut_frame.cut.get(),
            weld=self.parent.parent.left_frame.hole_weld_frame.hole_weld.get(),
            defects=self.parent.parent.left_frame.additional_info_frame.defects_frame.defects.get(),
            ultrasonic=self.parent.parent.left_frame.additional_info_frame.ultrasonic_frame.ultrasonic.get()
        )
        self._clear_calc_values()
        self.item = ItemFactory.build(data)
        self._set_calc_values(self.item)

    def save_pdf_callback(self):
        my_logger.info('save_pdf_callback')
        self.manual_calc_callback()
        render = RenderFactory.build(RenderTypeEnum.PDF)(self.item.title, PaperSize.A4_PORTRAIT)
        drawer = Drawer(render)
        self.item.draw_stamp(drawer)
        self.item.draw(drawer)
        render.save()

    def _clear_calc_values(self):
        self.parent.parent.calc_value_frame.calc_total_height.set('')
        self.parent.parent.calc_value_frame.calc_total_diameter.set('')
        self.parent.parent.calc_value_frame.calc_total_weight.set('')
        self.parent.parent.calc_value_frame.calc_total_pressure.set('')
        self.parent.parent.calc_value_frame.calc_total_k.set('')
        self.parent.parent.calc_value_frame.calc_total_k1.set('')

    def _set_calc_values(self, item):
        # try:
        calc_total_height = '%s мм' % round(item.get_total_height)
        calc_total_diameter = '%s мм' % round(item.get_total_diameter)
        calc_total_weight = '%s кг' % math.ceil(item.get_total_weight)
        calc_total_pressure = '{:.6f} МПа'.format(item.get_total_pressure)
        calc_total_k = '{:.2f}'.format(item.get_k)

        self.parent.parent.calc_value_frame.calc_total_height.set(calc_total_height)
        self.parent.parent.calc_value_frame.calc_total_diameter.set(calc_total_diameter)
        self.parent.parent.calc_value_frame.calc_total_weight.set(calc_total_weight)
        self.parent.parent.calc_value_frame.calc_total_pressure.set(calc_total_pressure)
        self.parent.parent.calc_value_frame.calc_total_k.set(calc_total_k)

        if item.data.item_form == ItemFormEnum.FLAT:
            calc_total_k1 = '{:.2f}'.format(item.get_k1)
            self.parent.parent.calc_value_frame.calc_total_k1.set(calc_total_k1)

    # except Exception as e:
    #     my_logger.info(f'Не удалось посчитать: {e}')
