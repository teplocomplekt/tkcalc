import cairo
import gi

from utils.settings import BASE_DIR, FONT

gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo

font_path = BASE_DIR / 'assets/font/GOST2304_TypeA.ttf'

def draw_text():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 400)
    context = cairo.Context(surface)

    pango_context = PangoCairo.create_context(context)
    layout = Pango.Layout(pango_context)



    font_desc = Pango.FontDescription(str(font_path))
    font_desc.set_family(FONT)  # Используйте имя шрифта из файла
    font_desc.set_size(40 * Pango.SCALE)     # Размер в пунктах (умножить на SCALE)
    font_desc.set_style(Pango.Style.ITALIC)  # Стиль (NORMAL, ITALIC, OBLIQUE)
    font_desc.set_weight(Pango.Weight.NORMAL)  # Насыщенность (NORMAL, BOLD)

    font_map = PangoCairo.font_map_get_default()
    try:
        font_map.load_font(pango_context, font_desc)
    except Exception as e:
        print(f"Ошибка загрузки шрифта: {e}")

    layout.set_font_description(font_desc)
    layout.set_text("⌀±10 Днище Пример текста с пользовательским шрифтом")

    # 6. Рисуем текст
    context.set_source_rgb(244, 0, 0)  # Черный цвет текста
    PangoCairo.show_layout(context, layout)

    # 7. Сохраняем результат
    surface.write_to_png("custom_font_example.png")
    print("Изображение сохранено как custom_font_example.png")

draw_text()