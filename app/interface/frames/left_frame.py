import tkinter
from tkinter import ttk

from interface.frames.additional_info_frame import AdditionalInfoFrame
from interface.frames.cone_input_frame import ConeInputFrame
from interface.frames.hole_weld_frame import HoleWeldFrame
from utils.settings import PAD


class LeftFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        self.additional_info_frame = AdditionalInfoFrame(self)
        self.additional_info_frame.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        self.hole_weld_frame = HoleWeldFrame(self)
        self.hole_weld_frame.grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)

        self.cone_input_frame = ConeInputFrame(self)
        self.cone_input_frame.grid(row=2, column=0, **PAD, sticky=tkinter.NSEW)
