__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import math


class Pulser(blinkyLib.Animation):
    """_summary_
    Pulser animation where a red light bounces form end to end with a trail
    """

    def __init__(self, led_count: int = 0):
        """
        Initializes a new instance of the Pulser class.

        Args:
            led_count (int, optional): The number of LEDs in this animation.
        """

        super().__init__(led_count)

        self._current = 0
        self._direction = 1

    def reset(self):
        self._current = 0
        self._direction = 1

    def led_value(self, led: int) -> blinkyLib.Color:
        # Light the current LED, and 2 behind it
        if led == self._current:
            return blinkyLib.Color.Red()
        elif led == self._current - self._direction:
            return blinkyLib.Color(20, 0, 0)
        elif led == self._current - (self._direction * 2):
            return blinkyLib.Color(7, 0, 0)
        else:
            return blinkyLib.Color.Black()

    def next_frame(self):
        # Swap directions if we're at the ends
        if self._direction == 1 and self._current == self.led_count - 1:
            self._direction = -self._direction
        elif self._direction == -1 and self._current == 0:
            self._direction = -self._direction

        # Move the pulse on one
        self._current = self._current + self._direction
