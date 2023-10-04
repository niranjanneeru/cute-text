from .consts import TINY_TEXT,BLACK_BUBBLE_TEXT, BUBBLE_TEXT, CURSIVE_TEXT
from .converters import TinyTextConverter, BlackBubbleTextConverter, BubbleTextConverter, CursiveTextConverter

class CuteTextConverter:
    def convert(self, text, format):
        return self._get_converter(format).convert(text)
    
    def _get_converter(self, format: TINY_TEXT):
        if format == TINY_TEXT:
            return TinyTextConverter()
        if format == BUBBLE_TEXT:
            return BubbleTextConverter()
        if format == BLACK_BUBBLE_TEXT:
            return BlackBubbleTextConverter()
        if format == CURSIVE_TEXT:
            return CursiveTextConverter()