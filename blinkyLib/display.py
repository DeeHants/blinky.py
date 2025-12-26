__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

from abc import ABC, abstractmethod
import time

from .constants import Consts
from .animation import Animation
from .frame import Frame


class Display:
    """
    Display interface class.
    """

    def __init__(self, led_count: int):
        """
        Initializes a new instance of the Display class.

        Args:
            led_count (int): The maximum number of LEDs to control.
        """

        # Save the details we can
        self._led_count = led_count

        # Save the LED count so it's used as the default count for all Frame objects
        Consts._lastLedCount = led_count

    @property
    def led_count(self) -> int:
        """Gets the number of LEDs in this display instance."""
        return self._led_count

    @abstractmethod
    def render_frame(self, frame: Frame):
        """
        Renders the frame on the display.

        Args:
            frame (Frame): The frame to render on the display.
        """
        raise NotImplementedError("Subclasses must implement render_frame method.")

    def animate(self, animation: Animation, interval: float, count: int):
        """
        Renders an animated frame on a loop.

        Args:
            animation (Animation): The animation to render on the display.
            interval (float): Interval to wait between frames in seconds.
            count (int): The number of frames to render. -1 to loop continuously.
        """

        animation.reset()
        index = 0

        while count == -1 or index < count:
            self.render_frame(animation)
            time.sleep(interval)
            animation.next_frame()
            if count >= 0:
                index = index + 1
