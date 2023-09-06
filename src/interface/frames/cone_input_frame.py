import tkinter
from tkinter import ttk

from interface.frames.mixins import LabeledEntryMixin, DisableMixin
from utils.settings import PAD


class ConeInputFrame(LabeledEntryMixin, DisableMixin, ttk.LabelFrame):
    def __init__(self, parent=None):
        super().__init__(parent, text='Коническое днище')

        self.alpha = tkinter.IntVar(value=90)
        self.Dm = tkinter.IntVar()

        ttk.Label(self, text='Угол α °').grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        frame = ttk.Frame(self)
        frame.grid(row=0, column=1)

        btn60 = ttk.Radiobutton(frame, text=60, value=60, variable=self.alpha)
        btn60.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        btn90 = ttk.Radiobutton(frame, text=90, value=90, variable=self.alpha)
        btn90.grid(row=0, column=1, **PAD, sticky=tkinter.NSEW)

        self.entry_with_label(parent=self, row=1, text='Dмал', variable=self.Dm)

        self.disable()
