__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import requests

from .Constants import Consts
from .Display import Display
from .Animation import Animation
from .Frame import Frame


class WLED(Display):
    """
    WLED interface class.
    The communication methods and details in this class are from the WLED docs:
    https://kno.wled.ge/interfaces/json-api/#per-segment-individual-led-control
    """

    def __init__(self, address: str, led_count: int = Consts.DEFAULT_LED_COUNT):
        """
        Initializes a new instance of the WLED class.

        Args:
            address (str): The WLED controller address to connect to.
            led_count (int, optional): The maximum number of LEDs to control. Defaults to Consts.DEFAULT_LED_COUNT.
        """

        super().__init__(led_count)

        # Save the address
        self._address = address

    def render_frame(self, frame: Frame):
        """
        Renders the frame on the WLED controller.

        Args:
            frame (Frame): The frame to render on the display.
        """

        # Build an array of hex RGB values for each LED in the frame
        cols = []
        for led in range(frame.led_count):
            led_color = frame.led_value(led)
            led_hex = format(led_color.to_value(), "06X")
            cols.append(led_hex)

        # Create state payload to set the LED/pixel states
        payload = {"seg": {"i": cols}}

        # Send the desired state to the controller
        result = self._send_state(payload)

    def _send_state(self, state: dict):
        url = f"http://{self._address}/json"
        response = requests.post(url, json=state)
        return response.json()
