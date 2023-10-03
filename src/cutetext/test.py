from .factory import CuteTextConverter, TINY_TEXT, BLACK_BUBBLE_TEXT, BUBBLE_TEXT

c = CuteTextConverter()._get_converter(TINY_TEXT)
print(c.convert("Hello"))

c = CuteTextConverter()._get_converter(BUBBLE_TEXT)
print(c.convert("Hello"))

c = CuteTextConverter()._get_converter(BLACK_BUBBLE_TEXT)
print(c.convert("Hello"))