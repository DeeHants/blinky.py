__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib


def get_display():
    return get_blinkytape_display()


def get_blinkytape_display():
    # Change the port and count to match your device
    serial_port = "COM9"
    led_count = 60
    return blinkyLib.BlinkyTape(serial_port, led_count)
