from abc import ABC, abstractmethod

from .Color import Color

class Frame(ABC):
    """
    Interface used by classes to provide the data for a single frame.
    """

    @property
    @abstractmethod
    def led_count(self):
        """Gets the number of LEDs in this frame."""
        return 0

    @abstractmethod
    def led_value(self, led):
        """
        Gets the color of an individual LED.

        Args:
            led (_type_): The 0 based index for the LED.

        Returns:
            _type_: Returns the Color value of the LED.
        """
        return Color.Black()
