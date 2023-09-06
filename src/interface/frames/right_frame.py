import tkinter
from tkinter import ttk

from interface.frames.action_buttons_frame import ActionButtonsFrame
from interface.frames.input_data_frame import InputDataFrame
from utils.settings import PAD


class RightFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        self.input_data_frame = InputDataFrame(self)
        self.input_data_frame.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        self.action_buttons_frame = ActionButtonsFrame(self)
        self.action_buttons_frame.grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)
