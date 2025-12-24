__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib
import test_device

# Connect to the strip
tape = test_device.get_display()

# Pulse
loops = 2
from Animations.Pulser import Pulser

animation = Pulser()
# tape.animate(animation, 0.02, ((animation.led_count - 1) * loops * 2) + 1)
tape.animate(animation, 0.02, -1)
