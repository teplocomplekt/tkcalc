PT2MM = 1 / 72 * 25.4
MM2PT = 72 / 25.4


class PaperSize:
    A4_PORTRAIT = (210, 297)
    A4_LANDSCAPE = (297, 210)

    @staticmethod
    def get_paper_in_pt(size: tuple):
        return map((lambda x: x * MM2PT), size)
