import tkinter
from tkinter import ttk

from utils.enums import ItemFormEnum
from utils.settings import PAD


class ItemFormFrame(ttk.LabelFrame):
    def __init__(self, parent=None):
        super().__init__(parent, text="Форма днища")

        self.variable = tkinter.StringVar(value=ItemFormEnum.default())

        for index, item in enumerate(ItemFormEnum):
            btn = ttk.Radiobutton(
                self,
                text=item,
                value=item,
                variable=self.variable,
                command=self.item_form_callback
            )
            btn.grid(
                row=index,
                column=0,
                **PAD,
                sticky=tkinter.NW
            )

    def item_form_callback(self):
        pass
