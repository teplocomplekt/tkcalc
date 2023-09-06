import tkinter
from tkinter import ttk

from interface.frames.mixins import LabeledEntryMixin


class InputDataFrame(LabeledEntryMixin, ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(1, weight=1)

        self.D = tkinter.IntVar()
        self.R = tkinter.IntVar()
        self.r = tkinter.IntVar()
        self.h = tkinter.IntVar()
        self.s = tkinter.IntVar()
        self.p = tkinter.IntVar()
        self.c1 = tkinter.DoubleVar()

        self.entry_with_label(parent=self, row=0, text='Dнр', variable=self.D)
        self.entry_with_label(parent=self, row=1, text='R', variable=self.R)
        self.entry_with_label(parent=self, row=3, text='r', variable=self.r)
        self.entry_with_label(parent=self, row=4, text='h', variable=self.h)
        self.entry_with_label(parent=self, row=5, text='s', variable=self.s)
        self.entry_with_label(parent=self, row=6, text='p', variable=self.p)
        self.entry_with_label(parent=self, row=7, text='c1', variable=self.c1)
