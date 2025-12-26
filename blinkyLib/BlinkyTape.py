__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import serial

from .Constants import Consts
from .Display import Display
from .Animation import Animation
from .Frame import Frame


class BlinkyTape(Display):
    """
    BlinkyTape interface class.
    The communication methods and details in this library are based on the PatternPaint sketch and color swirl:
    https://github.com/Blinkinlabs/PatternPaint/blob/master/src/PatternPaint/PatternPlayer_Sketch/PatternPlayer_Sketch.ino
    https://github.com/Blinkinlabs/PatternPaint/blob/master/src/PatternPaint/ColorSwirl_Sketch.h
    https://github.com/Blinkinlabs/BlinkyTape_Arduino/blob/master/examples/ColorSwirl/ColorSwirl.ino
    """

    DEFAULT_LED_COUNT: int = 60

    def __init__(self, port: str = "", led_count: int = DEFAULT_LED_COUNT):
        """
        Initializes a new instance of the BlinkyTape class.

        Args:
            port (str, optional): The COM port name to connect to. Defaults to ''.
            led_count (int, optional): The maximum number of LEDs to control. Defaults to DEFAULT_LED_COUNT.
        """

        super().__init__(led_count)

        # Try and open the port
        self.ser: serial.Serial = None
        if port != "":
            self.ser = serial.Serial(port, 115200)

    def render_frame(self, frame: Frame):
        """
        Renders the frame on the BlinkyTape.

        Args:
            frame (Frame): The frame to render on the BlinkyTape.
        """

        # Creates an array big enough to hold each LED color and the terminator.
        count = frame.led_count
        data_bytes = [0] * ((count + 1) * 3)
        for led in range(0, count):
            # 3 bytes, RGB, limited to a maximum of 254 as 255 is special.
            offset = led * 3
            led_color = frame.led_value(led)
            data_bytes[offset] = min(led_color.r, 254)
            data_bytes[offset + 1] = min(led_color.g, 254)
            data_bytes[offset + 2] = min(led_color.b, 254)

        # The sketch only reads three bytes at a time so send 3 with the final 0xFF
        offset = count * 3
        data_bytes[offset] = 0x0
        data_bytes[offset + 1] = 0x0
        data_bytes[offset + 2] = 0xFF

        # Send the data
        self.ser.write(data_bytes)
