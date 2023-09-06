import logging
import tkinter as tk

from interface.frames.item_form_frame import ItemFormFrame
from interface.frames.item_steel_frame import ItemSteelFrame
from interface.frames.left_frame import LeftFrame
from interface.frames.right_frame import RightFrame
from utils.settings import PAD

my_logger = logging.getLogger('my_logger')


class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.item_form_frame = ItemFormFrame(self)
        self.item_form_frame.grid(row=0, column=0, **PAD, sticky=tk.NSEW)

        self.item_steel_frame = ItemSteelFrame(self)
        self.item_steel_frame.grid(row=0, column=1, **PAD, sticky=tk.NSEW)

        self.left_frame = LeftFrame(self)
        self.left_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.right_frame = RightFrame(self)
        self.right_frame.grid(row=1, column=1, sticky=tk.NSEW)
