__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import math


class ColorSwirl(blinkyLib.Animation):
    """
    ColorSwirl animation taken from the original PatternPaint example.
    https://github.com/Blinkinlabs/BlinkyTape_Arduino/blob/master/examples/ColorSwirl/ColorSwirl.ino
    """

    def __init__(self, led_count: int = 60):
        """
        Initializes a new instance of the ColorSwirl class.

        Args:
            led_count (int, optional): The number of LEDs in this animation.
        """

        self._led_count = led_count

        self._rBal = 2
        self._gBal = 2
        self._bBal = 2

        self._j = 0
        self._f = 0
        self._k = 0

    @property
    def led_count(self) -> int:
        """Gets the number of LEDs in this frame."""
        return self._led_count

    def reset(self):
        self._j = 0
        self._f = 0
        self._k = 0

    def led_value(self, led: int) -> blinkyLib.Color:
        """
        Gets the color of an individual LED.

        Args:
            led (int): The 0 based index for the LED.

        Returns:
            Color: Returns the Color value of the LED.
        """
        r = 64.0 * (1.0 + math.sin(led / 2.0 + self._j / 4.0)) * self._rBal
        g = 64.0 * (1.0 + math.sin(led / 1.0 + self._f / 9.0 + 2.1)) * self._gBal
        b = 64.0 * (1.0 + math.sin(led / 3.0 + self._k / 14.0 + 4.2)) * self._bBal
        return blinkyLib.Color(int(r), int(g), int(b))

    def next_frame(self):
        self._j += 1
        self._f += 1
        self._k += 2
