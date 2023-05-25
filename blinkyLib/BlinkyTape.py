import serial

from .Constants import Consts
from .Frame import Frame

class BlinkyTape:
    lastLEDCount = Consts.DEFAULT_LED_COUNT

    def LastLEDCount():
        return BlinkyTape.lastLEDCount

    def __init__(self, port = '', led_count = Consts.DEFAULT_LED_COUNT):
        # Save the LED count so it's used as the default count for all Frame objects
        BlinkyTape.lastLedCount = led_count

        # Try and open the port
        self.ser = None
        if port != '':
            self.ser = serial.Serial(port, 115200)

    def render_frame(self, frame):
        # Creates an array big enough to hold each LED color and the terminator.
        count = frame.led_count
        data_bytes = [0] * ((count + 1) * 3)
        for led in range(0, count):
            # 3 bytes, RGB, limited to a maximum of 254 as 255 is special.
            offset = led * 3
            data_bytes[offset] = min(frame.led_value(led).r, 254)
            data_bytes[offset + 1] = min(frame.led_value(led).g, 254)
            data_bytes[offset + 2] = min(frame.led_value(led).b, 254)

        # The sketch only reads three bytes at a time so send 3 with the final 0xFF
        offset = count * 3
        data_bytes[offset] = 0x0
        data_bytes[offset + 1] = 0x0
        data_bytes[offset + 2] = 0xFF

        # Send the data
        self.ser.write(data_bytes)
