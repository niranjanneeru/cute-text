from abc import ABC, abstractmethod
from .maps import tiny_text_map, black_bubble_text_map, bubble_text_map, cursive_text_map, double_struck_text_map

class ConverterInterface(ABC):
    @abstractmethod
    def convert(self, text: str) -> str:
        pass

class TinyTextConverter(ConverterInterface):

    def convert(self, text: str) -> str:
        return text.translate(tiny_text_map)

class BubbleTextConverter(ConverterInterface):

    def convert(self, text: str) -> str:
        return text.translate(bubble_text_map)

class BlackBubbleTextConverter(ConverterInterface):

    def convert(self, text: str) -> str:
        return text.translate(black_bubble_text_map)

class CursiveTextConverter(ConverterInterface):

    def convert(self, text: str) -> str:
        return text.translate(cursive_text_map)

class DoubleStruckTextConverter(ConverterInterface):

    def convert(self, text: str) -> str:
        return text.translate(double_struck_text_map)
