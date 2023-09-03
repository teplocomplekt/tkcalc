import tkinter as tk
from tkinter import ttk

from utils.enums import ItemFormEnum, PAD, ItemSteelEnum


class ItemSteelWidget(ttk.LabelFrame):

    def __init__(self, text, variable, command=None, parent=None):
        super().__init__(parent, text=text)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        for index, item in enumerate(ItemSteelEnum):
            btn = ttk.Radiobutton(
                self,
                text=item,
                value=item,
                variable=variable,
                command=command
            )
            btn.grid(
                row=index // 2,
                column=1 if index % 2 > 0 else 0,
                **PAD,
                sticky=tk.NW
            )
