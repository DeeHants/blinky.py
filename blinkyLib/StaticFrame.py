__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

from .Constants import Consts
from .Color import Color
from .Frame import Frame


class StaticFrame(Frame):
    """
    Represents a single, static frame of LEDs.
    """

    def __init__(self, led_count: int = 0):
        """
        Initializes a new instance of the StaticFrame class.

        Args:
            led_count (int, optional): The number of LEDs in this frame.
        """

        super().__init__(led_count)

        self._leds = []
        for led in range(self.led_count):
            self._leds.append(Color.Black())

    def led_value(self, led: int) -> Color:
        """
        Gets the color of an individual LED.

        Args:
            led (int): The 0 based index for the LED.

        Returns:
            Color: Returns the Color value of the LED.
        """
        return self._leds[led]

    def set_range(self, start: int, end: int, color: Color):
        """
        Sets a range of LEDs to a single color.

        Args:
            start (int): The first LED of the range to set.
            end (int): The last LED of the range to set.
            color (Color): The color to set the LEDs to.
        """

        # Set all LEDs to the same color
        for led in range(start, end + 1):  # Remember it's exclusive
            self._leds[led] = color

    def set_range_fade(
        self, start: int, end: int, start_color: Color, end_color: Color
    ):
        """
        Sets a range of LEDs to a fade between two colors.

        Args:
            start (int): The first LED of the range to set.
            end (int): The last LED of the range to set.
            start_color (Color): The start LED color.
            end_color (Color): The end LED color.
        """

        # Calculate the steps and the amount to change
        steps = end - start
        redDelta = end_color.r - start_color.r
        redStep = redDelta / steps
        greenDelta = end_color.g - start_color.g
        greenStep = greenDelta / steps
        blueDelta = end_color.b - start_color.b
        blueStep = blueDelta / steps

        redRunning = start_color.r
        greenRunning = start_color.g
        blueRunning = start_color.b

        # Fill in the range
        for led in range(start, end + 1):  # Remember it's exclusive
            color = Color(int(redRunning), int(greenRunning), int(blueRunning))
            self._leds[led] = color

            redRunning += redStep
            greenRunning += greenStep
            blueRunning += blueStep

    @staticmethod
    def create_solid_frame(color: Color, led_count: int = 0) -> Frame:
        """
        Creates a frame with all LEDs at the same color.

        Args:
            color (Color): The color of all the LEDs.
            led_count (int, optional): The number of LEDs in this frame.

        Returns:
            Frame: Returns the full Frame object.
        """

        frame = StaticFrame(led_count)
        frame.set_range(0, frame.led_count - 1, color)
        return frame

    @staticmethod
    def create_fade_frame(
        color1: Color, color2: Color, led_count: int = 0
    ) -> Frame:
        """
        Creates a frame with a fade between two colors.

        Args:
            color1 (Color): The first LED color.
            color2 (Color): The last LED color.
            led_count (int, optional): The number of LEDs in this frame.

        Returns:
            Frame: Returns the full Frame object.
        """

        frame = StaticFrame(led_count)
        frame.set_range_fade(0, frame.led_count - 1, color1, color2)
        return frame
