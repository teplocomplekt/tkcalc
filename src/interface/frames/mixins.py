import tkinter
from tkinter import ttk

from utils.settings import PAD


class LabeledEntryMixin:

    def entry_with_label(self, *, parent, row, text, variable):
        ttk.Label(parent, text=text).grid(row=row, column=0, **PAD, sticky=tkinter.W)
        entry = ttk.Entry(parent, textvariable=variable, width=8)
        entry.grid(row=row, column=1, **PAD, sticky=tkinter.NSEW)


class DFrame(ttk.Frame):

    def enable(self, state='!disabled'):

        def cstate(widget):
            # Is this widget a container?
            if widget.winfo_children:
                # It's a container, so iterate through its children
                for w in widget.winfo_children():
                    # change its state
                    w.state((state,))
                    # and then recurse to process ITS children
                    cstate(w)

        cstate(self)

    def disable(self):
        self.enable('disabled')
