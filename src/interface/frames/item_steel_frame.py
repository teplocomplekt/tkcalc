import tkinter
from tkinter import ttk

from utils.enums import ItemSteelEnum
from utils.settings import PAD


class ItemSteelFrame(ttk.LabelFrame):
    def __init__(self, parent=None):
        super().__init__(parent, text="Сталь")

        self.variable = tkinter.StringVar(value=ItemSteelEnum.default())
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        for index, item in enumerate(ItemSteelEnum):
            btn = ttk.Radiobutton(
                self,
                text=item,
                value=item,
                variable=self.variable,
                command=None
            )
            btn.grid(
                row=index // 2,
                column=1 if index % 2 > 0 else 0,
                **PAD,
                sticky=tkinter.NW
            )
