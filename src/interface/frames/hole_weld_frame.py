import logging
import tkinter
from tkinter import ttk

from interface.frames.mixins import DisableMixin
from utils.enums import ItemHoleWeldEnum
from utils.settings import PAD

my_logger = logging.getLogger('my_logger')


class HoleWeldFrame(DisableMixin, ttk.LabelFrame):

    def hole_weld_callback(self):
        if self.hole_weld.get() == ItemHoleWeldEnum.WELD:
            self.d.set(value=0)
            my_logger.info('d = 0')
        elif self.hole_weld.get() == ItemHoleWeldEnum.HOLE_21:
            self.d.set(value=21)
            print('d = 21')
        elif self.hole_weld.get() == ItemHoleWeldEnum.HOLE_41:
            self.d.set(value=41)
            print('d = 41')
        elif self.hole_weld.get() == ItemHoleWeldEnum.CUSTOM:
            self.entry_d.delete(0, tkinter.END)
            self.entry_d.focus_set()

    def __init__(self, parent=None):
        super().__init__(parent, text='Технологическое отверстие')

        my_logger.info('hole_weld')

        self.hole_weld = tkinter.StringVar(value=ItemHoleWeldEnum.default())
        self.d = tkinter.IntVar()

        self.d.set(value=21)

        btn_weld = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.WELD,
            value=ItemHoleWeldEnum.WELD,
            variable=self.hole_weld,
            command=self.hole_weld_callback
        )
        btn_weld.grid(row=0, column=0, columnspan=3, **PAD, sticky=tkinter.NSEW)

        btn_21 = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.HOLE_21,
            value=ItemHoleWeldEnum.HOLE_21,
            variable=self.hole_weld,
            command=self.hole_weld_callback
        )
        btn_21.grid(row=1, column=0, columnspan=3, **PAD, sticky=tkinter.NSEW)

        btn_41 = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.HOLE_41,
            value=ItemHoleWeldEnum.HOLE_41,
            variable=self.hole_weld,
            command=self.hole_weld_callback
        )
        btn_41.grid(row=2, column=0, columnspan=3, **PAD, sticky=tkinter.NSEW)

        btn_custom = ttk.Radiobutton(
            self,
            text=ItemHoleWeldEnum.CUSTOM,
            value=ItemHoleWeldEnum.CUSTOM,
            variable=self.hole_weld,
            command=self.hole_weld_callback
        )
        btn_custom.grid(row=3, column=0, **PAD, sticky=tkinter.NSEW)

        self.entry_d = ttk.Entry(self, textvariable=self.d, width=4)
        self.entry_d.grid(row=3, column=1, **PAD, sticky=tkinter.NSEW)

        label_d = ttk.Label(self, text='мм')
        label_d.grid(row=3, column=2, **PAD, sticky=tkinter.NSEW)


