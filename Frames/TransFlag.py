__copyright__ = "Copyright Deanna Earley"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

import blinkyLib


class TransFlag(blinkyLib.StaticFrame):
    """
    Single frame with the trans pride flag.
    """

    def __init__(self):
        """
        Initializes a new instance of the TransFlag class.
        """

        super().__init__(60)

        blue = blinkyLib.Color(0x1E, 0x90, 0xFF)
        pink = blinkyLib.Color(0xFF, 0, 0xFF)
        white = blinkyLib.Color.White()

        # Trans pride
        self.set_range(0, 59, blue)
        self.set_range(12, 47, pink)
        self.set_range(24, 35, white)
