from .factory import CuteTextConverter, TINY_TEXT

c = CuteTextConverter()._get_converter(TINY_TEXT)
print(c.convert("Hello"))