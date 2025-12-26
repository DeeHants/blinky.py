__copyright__ = "Copyright Deanna Earley"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

from abc import ABC, abstractmethod

from .frame import Frame


class Animation(Frame):
    """
    Interface used by classes to provide the animation frame.
    """

    # led_count is a property from Frame

    # led_value is an abstract method from Frame

    @abstractmethod
    def reset(self):
        """
        Resets the animation back to its initial state.
        """

    @abstractmethod
    def next_frame(self):
        """
        Sets up the next frame of the animation.
        """
