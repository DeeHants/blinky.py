__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import socket

from .constants import Consts
from .display import Display
from .frame import Frame


class DDP(Display):
    """
    DDP (Distributed Display Protocol) interface class.
    The communication methods and details in this class are from the DDP specification:
    http://www.3waylabs.com/ddp/
    """

    def __init__(self, address: str, led_count: int):
        """
        Initializes a new instance of the DDP class.

        Args:
            address (str): The DDP device to send to.
            led_count (int): The maximum number of LEDs to control.
        """

        # Save the address
        self._address = address

        super().__init__(led_count)

        # Initial message sequence count
        self._sequence = 0

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self._sock.connect((self._address, 4048))

    def render_frame(self, frame: Frame):
        """
        Renders the frame on the DDP display device.

        Args:
            frame (Frame): The frame to render on the display.
        """

        # Creates an array big enough to hold the header and each LED color.
        count = frame.led_count
        data_bytes = [0] * (10 + (count * 3))
        for led in range(0, count):
            # 3 bytes, RGB, limited to a maximum of 254 as 255 is special.
            offset = 10 + (led * 3)
            led_color = frame.led_value(led)
            data_bytes[offset] = led_color.r
            data_bytes[offset + 1] = led_color.g
            data_bytes[offset + 2] = led_color.b

        # Add the header
        data_bytes[0] = 0b01000001  # V1, no timecode, push
        data_bytes[1] = self._sequence & 0xF  # Sequence number (lower 4 bits)
        self._sequence = (self._sequence + 1) % 16
        data_bytes[2] = 0b00001011  # RGB type, 8 bits per pixel element
        data_bytes[3] = 1  # Default output device
        # Bytes 4-7 are 0 (no offset)
        data_bytes[8] = (count * 3) >> 8  # Length high byte
        data_bytes[9] = (count * 3) & 0xFF  # Length low byte

        # Send the desired state to the display
        self._sock.send(bytes(data_bytes))

        # Debug output
        if Consts.DEBUG:
            hex = " ".join(format(x, "02X") for x in bytearray(data_bytes))
            print(
                "Length {length}: {data}".format(
                    length=len(data_bytes),
                    data=hex,
                )
            )
