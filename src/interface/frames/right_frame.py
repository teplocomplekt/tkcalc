import tkinter

from interface.frames.input_data_frame import InputDataFrame


class RightFrame(tkinter.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.config(background='blue')

        self.input_data_frame = InputDataFrame(self)
        self.input_data_frame.grid(row=0, column=0, sticky=tkinter.NSEW)
