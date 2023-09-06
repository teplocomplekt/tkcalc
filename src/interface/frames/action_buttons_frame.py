import tkinter
from tkinter import ttk

from utils.settings import PAD


class ActionButtonsFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        button_auto = ttk.Button(self, text='Рассчитать', command=self.auto_calc_callback)
        button_auto.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        button_manual = ttk.Button(self, text='Рассчитать вручную', command=self.manual_calc_callback)
        button_manual.grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)

        button_pdf = ttk.Button(self, text='Сохранить PDF', command=self.save_pdf_callback)
        button_pdf.grid(row=2, column=0, **PAD, sticky=tkinter.NSEW)

    def auto_calc_callback(self):
        ...

    def manual_calc_callback(self):
        ...

    def save_pdf_callback(self):
        ...
