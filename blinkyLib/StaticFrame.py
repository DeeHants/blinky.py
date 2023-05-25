from .Constants import Consts
from .BlinkyTape import BlinkyTape
from .Color import Color
from .Frame import Frame

class StaticFrame(Frame):
    def __init__(self, led_count = BlinkyTape.lastLEDCount):
        self.led_count = led_count
        self.leds = []
        for led in range(self.led_count):
            self.leds.append(Color.Black())

    def ledCount(self):
        return self.led_count

    def ledValue(self, led):
        return self.leds[led]

    def setRange(self, start, end, color):
        # Set all LEDs to the same color
        for led in range(start, end + 1): # Remember it's exclusive
            self.leds[led] = color

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
            self.leds[led] = color

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
