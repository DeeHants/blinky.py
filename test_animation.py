__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib

serial_port = 'COM6'
led_count = 60

# Connect to the strip
tape = blinkyLib.BlinkyTape(serial_port, led_count)

# Animation
import time
from blinkyLib.Sequence import Sequence
animation = Sequence()
animation.add_frames([
    blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Red()),
    blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Green()),
    blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Blue()),
])
tape.animate(animation, 1, 20)
