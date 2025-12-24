__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import test_device

# Connect to the strip
tape = blinkyLib.BlinkyTape(test_device.serial_port, test_device.led_count)

# Multi fade
frame = blinkyLib.StaticFrame()
led_count = frame.led_count
frame.set_range_fade(
    0, int(led_count / 2), blinkyLib.Color.Red(), blinkyLib.Color.Green()
)
frame.set_range_fade(
    int(led_count / 2), led_count - 1, blinkyLib.Color.Green(), blinkyLib.Color.Blue()
)
tape.render_frame(frame)
