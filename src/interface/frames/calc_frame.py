import tkinter
from tkinter import ttk

from utils.settings import PAD


class CalcLabelFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        ttk.Label(self, text='Общая высота днища') \
            .grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, text='Диаметр заготовки') \
            .grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, text='Масса готового днища') \
            .grid(row=2, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, text='Допускаемое внутренне давление') \
            .grid(row=3, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, text='Запас прочности', state=tkinter.DISABLED) \
            .grid(row=4, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, text='Запас прочности крышки', state=tkinter.DISABLED) \
            .grid(row=5, column=0, **PAD, sticky=tkinter.NSEW)


class CalcValueFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.calc_total_height = tkinter.StringVar()
        self.calc_total_diameter = tkinter.StringVar()
        self.calc_total_weight = tkinter.StringVar()
        self.calc_total_pressure = tkinter.StringVar()
        self.calc_total_k = tkinter.DoubleVar()
        self.calc_total_k1 = tkinter.DoubleVar()

        ttk.Label(self, textvariable=self.calc_total_height) \
            .grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, textvariable=self.calc_total_diameter) \
            .grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, textvariable=self.calc_total_weight) \
            .grid(row=2, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, textvariable=self.calc_total_pressure) \
            .grid(row=3, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, textvariable=self.calc_total_k, state=tkinter.DISABLED) \
            .grid(row=4, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Label(self, textvariable=self.calc_total_k1, state=tkinter.DISABLED) \
            .grid(row=5, column=0, **PAD, sticky=tkinter.NSEW)
