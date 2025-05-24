# Compilation mode, support OS-specific options

# nuitka-project: --jobs=-1

# nuitka-project-if: {OS} in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --onefile
# nuitka-project-else:
#    nuitka-project: --mode=standalonealone

# nuitka-project: --enable-plugin=tk-inter
# nuitka-project: --include-data-files=./app/assets/icon.png=assets/icon.png
# nuitka-project: --windows-icon-from-ico=./app/assets/icon.png

# nuitka-project-if: {OS} == "Windows" and os.getenv("DEBUG_COMPILATION", "no") == "yes":
#     nuitka-project: --windows-console-mode=hide
# nuitka-project-else:
#     nuitka-project: --windows-console-mode=disable


from tkinter import ttk

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
    root.wm_iconphoto(False, tk.PhotoImage(file=BASE_DIR / 'assets/icon.png'))

    root.mainloop()

    # app = App()
    # app.mainloop()


if __name__ == '__main__':
    main()
