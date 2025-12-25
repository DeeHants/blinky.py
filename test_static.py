__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import test_device

# Connect to the strip
tape = test_device.get_display()

# Static colour
purple = blinkyLib.Color.from_value(0x8800FF)
# colour = blinkyLib.Color.Black()
frame = blinkyLib.StaticFrame.create_solid_frame(purple)
tape.render_frame(frame)
