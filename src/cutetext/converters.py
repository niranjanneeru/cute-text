from abc import ABC, abstractmethod
from .maps import tiny_text_map, black_bubble_text, bubble_text_map

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
        return text.translate(black_bubble_text)