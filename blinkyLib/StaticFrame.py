from .Constants import Consts
from .BlinkyTape import BlinkyTape
from .Color import Color
from .Frame import Frame

class StaticFrame(Frame):
    """
    Represents a single, static frame of BlinkyTape LEDs.
    """

    def __init__(self, led_count = BlinkyTape.lastLEDCount):
        """
        Initializes a new instance of the StaticFrame class.

        Args:
            led_count (_type_, optional): The number of LEDs in this frame. Defaults to BlinkyTape.lastLEDCount.
        """

        self._led_count = led_count
        self._leds = []
        for led in range(self._led_count):
            self._leds.append(Color.Black())

    @property
    def led_count(self):
        """Gets the number of LEDs in this frame."""
        return self._led_count

    def led_value(self, led):
        """
        Gets the color of an individual LED.

        Args:
            led (_type_): The 0 based index for the LED.

        Returns:
            _type_: Returns the Color value of the LED.
        """
        return self._leds[led]

    def set_range(self, start, end, color):
        """
        Sets a range of LEDs to a single color.

        Args:
            start (_type_): The first LED of the range to set.
            end (_type_): The last LED of the range to set.
            color (_type_): The color to set the LEDs to.
        """

        # Set all LEDs to the same color
        for led in range(start, end + 1): # Remember it's exclusive
            self._leds[led] = color

    def set_range_fade(self, start, end, start_color, end_color):
        """
        Sets a range of LEDs to a fade between two colors.

        Args:
            start (_type_): The first LED of the range to set.
            end (_type_): The last LED of the range to set.
            start_color (_type_): The start LED color.
            end_color (_type_): The end LED color.
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
        for led in range(start, end + 1): # Remember it's exclusive
            color = Color(redRunning, greenRunning, blueRunning)
            self._leds[led] = color

            redRunning += redStep
            greenRunning += greenStep
            blueRunning += blueStep

    def create_solid_frame(color, led_count = BlinkyTape.LastLEDCount()):
        """
        Creates a frame with all LEDs at the same color.

        Args:
            color (_type_): The color of all the LEDs.
            led_count (_type_, optional): The number of LEDs in this frame. Defaults to BlinkyTape.LastLEDCount().

        Returns:
            _type_: Returns the full Frame object.
        """

        frame = StaticFrame(led_count)
        frame.set_range(0, led_count - 1, color)
        return frame

    def create_fade_frame(color1, color2, led_count = BlinkyTape.lastLEDCount):
        """
        Creates a frame with a fade between two colors.

        Args:
            color1 (_type_): The first LED color.
            color2 (_type_): The last LED color.
            led_count (_type_, optional): The number of LEDs in this frame. Defaults to BlinkyTape.lastLEDCount.

        Returns:
            _type_: Returns the full Frame object.
        """

        frame = StaticFrame(led_count)
        frame.set_range_fade(0, led_count - 1, color1, color2)
        return frame
