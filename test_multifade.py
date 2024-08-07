__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib

serial_port = "COM6"
led_count = 60

# Connect to the strip
tape = blinkyLib.BlinkyTape(serial_port, led_count)

# Multi fade
frame = blinkyLib.StaticFrame()
frame.set_range_fade(
    0, int(led_count / 2),
    blinkyLib.Color.Red(),
    blinkyLib.Color.Green()
)
frame.set_range_fade(
    int(led_count / 2), led_count - 1,
    blinkyLib.Color.Green(),
    blinkyLib.Color.Blue()
)
tape.render_frame(frame)
