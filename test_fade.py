__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib

serial_port = 'COM6'
led_count = 60

# Connect to the strip
tape = blinkyLib.BlinkyTape(serial_port, led_count)

# Fade
frame = blinkyLib.StaticFrame.create_fade_frame(
    blinkyLib.Color.Red(),
    blinkyLib.Color.Green()
)
tape.render_frame(frame)
