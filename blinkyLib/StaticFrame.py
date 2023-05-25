from .Constants import Consts
from .BlinkyTape import BlinkyTape
from .Color import Color
from .Frame import Frame

class StaticFrame(Frame):
    def __init__(self, led_count = BlinkyTape.lastLEDCount):
        self._led_count = led_count
        self._leds = []
        for led in range(self._led_count):
            self._leds.append(Color.Black())

    @property
    def led_count(self):
        return self._led_count

    def led_value(self, led):
        return self._leds[led]

    def set_range(self, start, end, color):
        # Set all LEDs to the same color
        for led in range(start, end + 1): # Remember it's exclusive
            self._leds[led] = color

    def set_range_fade(self, start, end, startColor, endColor):
        # Calculate the steps and the amount to change
        steps = end - start
        redDelta = endColor.r - startColor.r
        redStep = redDelta / steps
        greenDelta = endColor.g - startColor.g
        greenStep = greenDelta / steps
        blueDelta = endColor.b - startColor.b
        blueStep = blueDelta / steps

        redRunning = startColor.r
        greenRunning = startColor.g
        blueRunning = startColor.b

        # Fill in the range
        for led in range(start, end + 1): # Remember it's exclusive
            color = Color(redRunning, greenRunning, blueRunning)
            self._leds[led] = color

            redRunning += redStep
            greenRunning += greenStep
            blueRunning += blueStep

    def create_solid_frame(color, led_count = BlinkyTape.LastLEDCount()):
        frame = StaticFrame(led_count)
        frame.set_range(0, led_count - 1, color)
        return frame

    def create_fade_frame(color1, color2, led_count = BlinkyTape.lastLEDCount):
        frame = StaticFrame(led_count)
        frame.set_range_fade(0, led_count - 1, color1, color2)
        return frame
