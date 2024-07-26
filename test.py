__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib

serial_port = 'COM6'
led_count = 60

# Connect to the strip
tape = blinkyLib.BlinkyTape(serial_port, led_count)

# Static colour
purple = blinkyLib.Color(128, 0, 255)
# colour = blinkyLib.Color.Black()
frame = blinkyLib.StaticFrame.create_solid_frame(purple)
tape.render_frame(frame)

# Fade
frame = blinkyLib.StaticFrame.create_fade_frame(
    blinkyLib.Color.Red(),
    blinkyLib.Color.Green()
)
tape.render_frame(frame)

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

# Pride flag
from Frames.PrideFlag import PrideFlag
frame = PrideFlag()
tape.render_frame(frame)

# Animation
import time
from blinkyLib.Sequence import Sequence
animation = Sequence()
animation.add_frames([
    blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Red()),
    blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Green()),
    blinkyLib.StaticFrame.create_solid_frame(blinkyLib.Color.Blue()),
])
animation.reset()
for index in range(20):
    tape.render_frame(animation)
    time.sleep(1)
    animation.next_frame()
