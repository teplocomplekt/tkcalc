import logging
import tkinter
from tkinter import ttk

from items.item import ItemFactory
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
        self.item = ItemFactory.build_item(self.parent.parent.item_form_frame.variable.get())

    def save_pdf_callback(self):
        my_logger.info('save_pdf_callback')
        self.manual_calc_callback()
