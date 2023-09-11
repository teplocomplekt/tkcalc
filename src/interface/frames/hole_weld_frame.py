import tkinter
from tkinter import ttk

from interface.frames.mixins import DisableMixin
from utils.enums import ItemHoleWeldEnum
from utils.settings import PAD


class HoleWeldFrame(DisableMixin, ttk.LabelFrame):
    def __init__(self, parent=None):
        super().__init__(parent, text='Технологическое отверстие')

        self.hole_weld = tkinter.StringVar(value=ItemHoleWeldEnum.default())
        self.d = tkinter.IntVar()

        btn_weld = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.WELD,
            value=ItemHoleWeldEnum.WELD,
            variable=self.hole_weld
        )
        btn_weld.grid(row=0, column=0, columnspan=3, **PAD, sticky=tkinter.NSEW)

        btn_21 = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.HOLE_21,
            value=ItemHoleWeldEnum.HOLE_21,
            variable=self.hole_weld
        )
        btn_21.grid(row=1, column=0, columnspan=3, **PAD, sticky=tkinter.NSEW)

        btn_41 = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.HOLE_41,
            value=ItemHoleWeldEnum.HOLE_41,
            variable=self.hole_weld
        )
        btn_41.grid(row=2, column=0, columnspan=3, **PAD, sticky=tkinter.NSEW)

        btn_custom = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.CUSTOM,
            value=ItemHoleWeldEnum.CUSTOM,
            variable=self.hole_weld
        )
        btn_custom.grid(row=3, column=0, **PAD, sticky=tkinter.NSEW)

        entry_d = ttk.Entry(self, textvariable=self.d, width=4)
        entry_d.grid(row=3, column=1, **PAD, sticky=tkinter.NSEW)

        label_d = ttk.Label(self, text='мм')
        label_d.grid(row=3, column=2, **PAD, sticky=tkinter.NSEW)
