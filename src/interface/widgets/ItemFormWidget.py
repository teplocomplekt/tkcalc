import tkinter as tk
from tkinter import ttk

from utils.enums import ItemFormEnum, PAD


class ItemFormWidget(ttk.LabelFrame):

    def __init__(self, text, variable, command, parent=None):
        super().__init__(parent, text = text)
        for index, item in enumerate(ItemFormEnum):
            btn = ttk.Radiobutton(
                self,
                text=item,
                value=item,
                variable=variable,
                command=command
            )
            btn.grid(
                row=index,
                column=0,
                **PAD,
                sticky=tk.NW
            )
