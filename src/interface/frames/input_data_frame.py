import tkinter
from tkinter import ttk

from utils.settings import PAD


class InputDataFrame(tkinter.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(1, weight=1)
        self.config(background='pink')

        self.D = tkinter.StringVar()
        self.R = tkinter.StringVar()

        self.entry_with_label(0, 'Dнр', self.D)
        self.entry_with_label(1, 'R', self.R)

    def entry_with_label(self, row, label, variable):
        ttk.Label(self, text=label).grid(row=row, column=0, **PAD, sticky=tkinter.W)
        self.entry = tkinter.Entry(self, textvariable=variable, width=8)
        self.entry.grid(row=row, column=1, **PAD, sticky=tkinter.NSEW)
