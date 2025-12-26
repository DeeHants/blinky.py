__copyright__ = "Copyright Deanna Earley"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import test_device

# Connect to the strip
tape = test_device.get_display()

# Fade
frame = blinkyLib.StaticFrame.create_fade_frame(
    blinkyLib.Color.Red(), blinkyLib.Color.Green()
)
tape.render_frame(frame)
