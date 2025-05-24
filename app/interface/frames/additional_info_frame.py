import tkinter
from tkinter import ttk

from interface.frames.mixins import LabeledEntryMixin
from utils.settings import PAD


class ChamferFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.chamfer = tkinter.BooleanVar()
        self.chamfer_value = tkinter.IntVar(value=45)

        ttk.Checkbutton(
            self,
            text='Фаска',
            variable=self.chamfer,
            command=self.chamfer_callback
        ).grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        ttk.Entry(
            self,
            textvariable=self.chamfer_value,
            width=4
        ).grid(row=0, column=1, **PAD, sticky=tkinter.NSEW)

        ttk.Label(
            self,
            text='градусов'
        ).grid(row=0, column=2, **PAD, sticky=tkinter.NSEW)

    def chamfer_callback(self):
        state = self.chamfer.get()
        if state:
            self.parent.cut_frame.cut.set(value=True)
            self.parent.cut_frame.btn.config(state=tkinter.DISABLED)
        else:
            self.parent.cut_frame.cut.set(value=False)
            self.parent.cut_frame.btn.config(state=tkinter.NORMAL)


class CutFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cut = tkinter.BooleanVar()
        self.btn = ttk.Checkbutton(self, text='Подрезка/Торцовка', variable=self.cut)
        self.btn.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)


class DefectsFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.defects = tkinter.BooleanVar()
        btn = ttk.Checkbutton(self, text='Дефектоскопия', variable=self.defects)
        btn.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)


class UltrasonicFrame(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ultrasonic = tkinter.BooleanVar()
        btn = ttk.Checkbutton(self, text='УЗК', variable=self.ultrasonic)
        btn.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)


class AdditionalInfoFrame(LabeledEntryMixin, ttk.LabelFrame):
    def __init__(self, parent=None):
        super().__init__(parent, text='Дополнительные услуги')

        self.alpha = tkinter.IntVar(value=90)

        self.chamfer = ChamferFrame(self)
        self.chamfer.grid(row=0, column=0, **PAD, sticky=tkinter.NSEW)

        self.cut_frame = CutFrame(self)
        self.cut_frame.grid(row=1, column=0, **PAD, sticky=tkinter.NSEW)

        self.defects_frame = DefectsFrame(self)
        self.defects_frame.grid(row=2, column=0, **PAD, sticky=tkinter.NSEW)

        self.ultrasonic_frame = UltrasonicFrame(self)
        self.ultrasonic_frame.grid(row=3, column=0, **PAD, sticky=tkinter.NSEW)
