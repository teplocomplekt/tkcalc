#!/bin/env python3

from interface.gui import App
# from interface.gui import App
import tkinter as tk

from utils.settings import APP_TITLE, BASE_DIR


def main():
    root = tk.Tk()
    app = App(root)
    app.pack()
    # устанавливаем заголовок окна
    root.title(APP_TITLE)
    # Запрещаем fullscreen
    root.resizable(False, False)
    # Иконка
    root.wm_iconphoto(False, tk.PhotoImage(file=BASE_DIR / 'icon.png'))

    root.mainloop()

    # app = App()
    # app.mainloop()


if __name__ == '__main__':
    main()
