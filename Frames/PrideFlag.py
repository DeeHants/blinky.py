__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib

class PrideFlag(blinkyLib.StaticFrame):
    """
    Single frame with the 6 stripe pride flag.
    """

    def __init__(self, faded: bool = False):
        """
        Initializes a new instance of the PrideFlag class.

        Args:
            faded (bool, optional): Whether to fade between the colours sections
        """

        blinkyLib.StaticFrame.__init__(self)

        purple = blinkyLib.Color(128, 0, 128)
        blue = blinkyLib.Color.Blue()
        green = blinkyLib.Color.Green()
        yellow = blinkyLib.Color(255, 255, 0)
        orange = blinkyLib.Color(255, 128, 0)
        red = blinkyLib.Color.Red()

        # Pride rainbow
        self.set_range(0, 9, purple)
        self.set_range(10, 19, blue)
        self.set_range(20, 29, green)
        self.set_range(30, 39, yellow)
        self.set_range(40, 49, orange)
        self.set_range(50, 59, red)

        # Fade for 2 LEDs over each boundary
        if (faded):
            self.set_range_fade(8, 11, purple, blue)
            self.set_range_fade(18, 21, blue, green)
            self.set_range_fade(28, 31, green, yellow)
            self.set_range_fade(38, 41, yellow, orange)
            self.set_range_fade(48, 51, orange, red)
