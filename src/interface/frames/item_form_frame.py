import tkinter
from tkinter import ttk

from utils.enums import ItemFormEnum
from utils.settings import PAD


class ItemFormFrame(ttk.LabelFrame):
    def __init__(self, parent=None):
        super().__init__(parent, text="Форма днища")
        self.parent = parent

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
        form = self.variable.get()
        if form == ItemFormEnum.THORSPHERICAL:
            self.parent.left_frame.cone_input_frame.disable()
            self.parent.left_frame.hole_weld_frame.enable()
            marks = {
                'D': True,
                'R': True,
                'r': True,
                'h': True,
                's': True,
                'p': True,
                'c': True,
            }
            self.parent.right_frame.input_data_frame.mark_entries_state(marks=marks)
            # self.disableChildren(self.input_cone_frame)
            # self.label_total_k1.configure(state=tk.DISABLED)
            # self.label_calc_total_k1.configure(state=tk.DISABLED)
        elif form == ItemFormEnum.SPHERICAL:
            self.parent.left_frame.cone_input_frame.disable()
            self.parent.left_frame.hole_weld_frame.enable()
            marks = {
                'D': True,
                'R': True,
                'r': False,
                'h': False,
                's': True,
                'p': True,
                'c': True,
            }
            self.parent.right_frame.input_data_frame.mark_entries_state(marks=marks)
        # marks = {
        #     'D': True,
        #     'R': True,
        #     'r': False,
        #     's': True,
        #     'h': False,
        # }
        # # self.r.set('0')
        # # self.h.set('0')
        # self.mark_entries_state(marks=marks)
        # self.disableChildren(self.input_cone_frame)
        # self.label_total_k1.configure(state=tk.DISABLED)
        # self.label_calc_total_k1.configure(state=tk.DISABLED)
        elif form == ItemFormEnum.FLAT:
            self.parent.left_frame.cone_input_frame.disable()
            self.parent.left_frame.hole_weld_frame.enable()
            marks = {
                'D': True,
                'R': False,
                'r': True,
                'h': True,
                's': True,
                'p': True,
                'c': True,
            }
            self.parent.right_frame.input_data_frame.mark_entries_state(marks=marks)
        # marks = {
        #     'D': True,
        #     'R': False,
        #     'r': True,
        #     's': True,
        #     'h': True,
        # }
        # # self.R.set('1000000')
        # self.mark_entries_state(marks=marks)
        # self.disableChildren(self.input_cone_frame)
        # self.label_total_k1.configure(state=tk.NORMAL)
        # self.label_calc_total_k1.configure(state=tk.NORMAL)

        elif form == ItemFormEnum.CONE:
            self.parent.left_frame.cone_input_frame.enable()
            self.parent.left_frame.hole_weld_frame.disable()
            marks = {
                'D': True,
                'R': False,
                'r': True,
                'h': True,
                's': True,
                'p': True,
                'c': True,
            }
            self.parent.right_frame.input_data_frame.mark_entries_state(marks=marks)
        # marks = {
        #     'D': True,
        #     'R': False,
        #     'r': True,
        #     's': True,
        #     'h': True,
        # }
        # self.mark_entries_state(marks=marks)
        # self.enableChildren(self.input_cone_frame)
        # self.label_total_k1.configure(state=tk.DISABLED)
        # self.label_calc_total_k1.configure(state=tk.DISABLED)
