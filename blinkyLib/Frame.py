from abc import ABC, abstractmethod

from .Color import Color

class Frame(ABC):
    @property
    @abstractmethod
    def led_count(self):
        return 0

    @abstractmethod
    def led_value(self, led):
        return Color.Black()
