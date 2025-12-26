__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib


# Change the details to match your device
def get_display():
    # # BlinkyTape on a serial port
    # return blinkyLib.BlinkyTape("COM3", 60)

    # # WLED controller
    # return blinkyLib.WLED("192.168.1.69") # Auto detect LED count

    # DDP interface to a WLED controller
    wled = blinkyLib.WLED("192.168.1.69") # Auto detect LED count
    return blinkyLib.DDP("192.168.1.69", wled.led_count)
