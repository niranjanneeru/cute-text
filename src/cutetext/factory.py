from . import TINY_TEXT, tiny_text_map, TinyTextConverter
import typing

class CuteTextConverter:
    def _get_converter(self, format: TINY_TEXT):
        if format == TINY_TEXT:
            return TinyTextConverter()
    
    def _convert_to_cute_text(self, text: str) -> str:
        return text.translate(tiny_text_map)