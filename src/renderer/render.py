import logging
from abc import abstractmethod
from enum import Enum

import cairo

from renderer.drawer import Drawer
from renderer.utils import PaperSize, MM2PT
from tkinter import filedialog

my_logger = logging.getLogger('my_logger')


class AbstractRender:
    surface = None
    context = None

    def __init__(self, filename: str, size: tuple[int]):
        self.size = size
        self.filename = filename

        self.init_surface()
        self.init_context()
        self.init_callback()
        matrix = cairo.Matrix(yy=-1)
        self.context.transform(matrix)
        self.context.set_font_matrix(matrix)

        # self.drawer = Drawer(render=self)

    @abstractmethod
    def init_surface(self):
        raise NotImplementedError()

    def init_context(self):
        self.context = cairo.Context(self.surface)

    def init_callback(self):
        pass

    @abstractmethod
    def save(self):
        raise NotImplementedError()


class RenderTypeEnum(str, Enum):
    PDF = 'pdf'


class PdfRender(AbstractRender):
    def __init__(self, filename, size):
        super().__init__(filename, size=size)

    def init_surface(self):

        file = filedialog.asksaveasfilename(
            initialfile=self.filename,
            filetypes=[('PDF file', '*.pdf')],
            defaultextension='.pdf'
        )
        self.surface = cairo.PDFSurface(file, *PaperSize.get_paper_in_pt(self.size))

    def save(self):
        my_logger.info('Сохранен PDF')
        try:
            self.surface.show_page()
        except Exception as e:
            print(f'Ошибка: {e}')

    def init_callback(self):
        self.context.scale(MM2PT, MM2PT)


class RenderFactory:

    @staticmethod
    def build(render_type: RenderTypeEnum) -> type[AbstractRender]:
        if render_type == RenderTypeEnum.PDF:
            return PdfRender
