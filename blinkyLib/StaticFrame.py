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

    def setRange(self, start, end, color):
        # Set all LEDs to the same color
        for led in range(start, end + 1): # Remember it's exclusive
            self._leds[led] = color

    def setRangeFade(self, start, end, startColor, endColor):
        # Calculate the steps and the amount to change
        steps = end - start
        redDelta = endColor.R() - startColor.R()
        redStep = redDelta / steps
        greenDelta = endColor.G() - startColor.G()
        greenStep = greenDelta / steps
        blueDelta = endColor.B() - startColor.B()
        blueStep = blueDelta / steps

        redRunning = startColor.R()
        greenRunning = startColor.G()
        blueRunning = startColor.B()

        # Fill in the range
        for led in range(start, end + 1): # Remember it's exclusive
            color = Color(redRunning, greenRunning, blueRunning)
            self._leds[led] = color

            redRunning += redStep
            greenRunning += greenStep
            blueRunning += blueStep

    def CreateSolidFrame(color, led_count = BlinkyTape.LastLEDCount()):
        frame = StaticFrame(led_count)
        frame.setRange(0, led_count - 1, color)
        return frame

    def CreateFade(color1, color2, led_count = BlinkyTape.lastLEDCount):
        frame = StaticFrame(led_count)
        frame.setRangeFade(0, led_count - 1, color1, color2)
        return frame
