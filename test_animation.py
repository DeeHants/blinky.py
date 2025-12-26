__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import test_device

# Connect to the strip
tape = test_device.get_display()

# Animation
animation = blinkyLib.Sequence()
animation.add_frames(
    [
        blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Red()),
        blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Green()),
        blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Blue()),
    ]
)
tape.animate(animation, 1, 15)
