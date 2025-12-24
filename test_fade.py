__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import test_device

# Connect to the strip
tape = blinkyLib.BlinkyTape(test_device.serial_port, test_device.led_count)

# Fade
frame = blinkyLib.StaticFrame.create_fade_frame(
    blinkyLib.Color.Red(), blinkyLib.Color.Green()
)
tape.render_frame(frame)
