from abc import ABC, abstractmethod
from datetime import date
import cairo
from tkinter import filedialog
import logging
from utils.settings import *
from render.utils import MM2PT, PaperSize
# from render.drawer import Drawer

my_logger = logging.getLogger('my_logger')


class BaseRender(ABC):
    surface = None

    def __init__(self):
        matrix = cairo.Matrix(yy=-1)
        self.context.transform(matrix)
        self.context.set_font_matrix(matrix)

    def draw_stamp(self):
        # Фон
        # self.context.set_source_rgb(0.9, 0.9, 0.5)
        # self.context.rectangle(0, 0, 210, 297)
        # self.context.fill()

        # Задаем стиль линии
        # self.context.set_source_rgb(0.0, 0.0, 0.0)
        # self.context.set_line_width(Drawer.LineWidth.MEDIUM)
        ...

    def save(self):
        my_logger.info('Сохранен PDF')
        try:
            self.surface.show_page()
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    @abstractmethod
    def get_render():
        pass


class PDFRender(BaseRender):

    def __init__(self, size, filename):
        self.size = size

        file = filedialog.asksaveasfilename(
            # initialdir=settings.BASE_DIR,
            initialfile=filename,
            filetypes=[('PDF file', '*.pdf')],
            defaultextension='.pdf'
        )

        self.surface = cairo.PDFSurface(file, *PaperSize.get_paper_in_pt(size))
        self.context = cairo.Context(self.surface)
        super().__init__()
        self.context.scale(MM2PT, MM2PT)

    def get_render(self):
        return self


class SVGRender(BaseRender):

    def __init__(self, size=PaperSize.A4_LANDSCAPE):
        self.size = size
        self.surface = cairo.SVGSurface('test.svg', *PaperSize.get_paper_in_pt(size))
        self.context = cairo.Context(self.surface)
        super().__init__()
        self.context.scale(MM2PT, MM2PT)

    def get_render(self):
        return self


class PNGRender(BaseRender):

    def __init__(self, size=(800, 600)):
        self.size = size
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *size)
        self.context = cairo.Context(self.surface)
        # self.context.scale(MM2PT, MM2PT)
        super().__init__()

    def save(self):
        # self.draw_stamp()
        self.surface.write_to_png("test.png")

    def get_render(self):
        return self


class Render:
    # render_types = {
    #     'PDF': PDFRender(),
    #     'SVG': PDFRender(),
    #     'PNG': PDFRender()
    # }

    @staticmethod
    def get_render(render_type, filename, size=PaperSize.A4_PORTRAIT):
        if render_type == 'PDF':
            return PDFRender(size, filename)
        if render_type == 'SVG':
            return SVGRender(size)
        if render_type == 'PNG':
            return PNGRender(size)
        return None
