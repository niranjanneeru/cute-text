from .consts import TINY_TEXT,BLACK_BUBBLE_TEXT, BUBBLE_TEXT
from .converters import TinyTextConverter, BlackBubbleTextConverter, BubbleTextConverter

class CuteTextConverter:
    def _get_converter(self, format: TINY_TEXT):
        if format == TINY_TEXT:
            return TinyTextConverter()
        if format == BUBBLE_TEXT:
            return BubbleTextConverter()
        if format == BLACK_BUBBLE_TEXT:
            return BlackBubbleTextConverter()