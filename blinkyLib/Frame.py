from abc import ABC, abstractmethod

from .Color import Color

class Frame(ABC):
    @abstractmethod
    def ledCount(self):
        return 0

    @abstractmethod
    def ledValue(self, led):
        return Color.Black()
