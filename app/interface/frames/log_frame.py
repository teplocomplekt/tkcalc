import logging
import tkinter
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from utils.logger import MyHandlerText

my_logger = logging.getLogger('my_logger')


class LogFrame(tkinter.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        # self.logtext = tkinter.Text(self, state="disabled", width=50, height=5)
        self.logtext = ScrolledText(self, state="disabled", width=50, height=5)
        # self.logtext.pack()
        self.logtext.grid(sticky=tkinter.NSEW)

        stderrHandler = logging.StreamHandler()  # no arguments => stderr
        my_logger.addHandler(stderrHandler)
        guiHandler = MyHandlerText(self.logtext)
        my_logger.addHandler(guiHandler)
        my_logger.setLevel(logging.INFO)

    def clear_log(self):
        self.logtext.configure(state='normal')
        self.logtext.delete("1.0", tkinter.END)
        self.logtext.configure(state='disabled')
