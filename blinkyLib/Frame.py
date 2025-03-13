__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

from abc import ABC, abstractmethod

from .Constants import Consts
from .Color import Color


class Frame(ABC):
    """
    Interface used by classes to provide the data for a single frame.
    """

    def __init__(self, led_count: int = 0):
        """
        Initializes a new instance of the Frame class.

        Args:
            led_count (int, optional): The number of LEDs in this frame.
        """

        if led_count == 0:
            led_count = Consts._lastLedCount
        self._led_count = led_count

    @property
    def led_count(self) -> int:
        """Gets the number of LEDs in this frame."""
        return self._led_count

    @abstractmethod
    def led_value(self, led: int) -> Color:
        """
        Gets the color of an individual LED.

        Args:
            led (int): The 0 based index for the LED.

        Returns:
            Color: Returns the Color value of the LED.
        """
        return Color.Black()
