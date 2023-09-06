import logging
import tkinter
from tkinter import ttk

from utils.logger import MyHandlerText

my_logger = logging.getLogger('my_logger')


class LogFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.logtext = tkinter.Text(self, state="disabled", width=50, height=5)
        self.logtext.pack()

        stderrHandler = logging.StreamHandler()  # no arguments => stderr
        my_logger.addHandler(stderrHandler)
        guiHandler = MyHandlerText(self.logtext)
        my_logger.addHandler(guiHandler)
        my_logger.setLevel(logging.INFO)
