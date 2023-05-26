__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

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
    def led_value(self, led: int):
        """
        Gets the color of an individual LED.

        Args:
            led (int): The 0 based index for the LED.

        Returns:
            Color: Returns the Color value of the LED.
        """
        return Color.Black()
