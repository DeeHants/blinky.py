__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"

from .Constants import Consts
from .BlinkyTape import BlinkyTape
from .Color import Color
from .Frame import Frame
from .Animation import Animation

class Sequence(Animation):
    """
    Animated sequence of frames
    """

    def __init__(self, led_count: int = BlinkyTape.lastLEDCount):
        """
        Initializes a new instance of the Strobe class.

        Args:
            led_count (int, optional): The number of LEDs in this frame. Defaults to BlinkyTape.lastLEDCount.
        """

        self._led_count = led_count
        self._frames = []
        self._frame_index = -1
        self._frame = None

    @property
    def led_count(self):
        """Gets the number of LEDs in this frame."""
        return self._led_count

    def led_value(self, led: int):
        """
        Gets the color of an individual LED.

        Args:
            led (int): The 0 based index for the LED.

        Returns:
            Color: Returns the Color value of the LED.
        """
        return Color.Black() if self._frame is None else self._frame.led_value(led)

    def reset(self):
        """
        Resets the sequence back to its initial state.
        """
        if len(self._frames) == 0:
            # If there are no frames, set the current index back to -1
            self._frame_index = -1
        else:
            # Set the current index to the first frame
            self._frame_index = 0

            # Get the new frame data
            self._frame = self._frames[self._frame_index]


    def add_frame(self, frame: Frame):
        """
        Adds a single frame to the sequence.

        Args:
            frame (Frame): The frame to add to the sequence.
        """
        # Add the frame
        self._frames.append(frame)

        # If this was the first frame, call next_frame to set things up
        if self._frame_index == -1:
            self.next_frame()

    def add_frames(self, frames: list):
        """
        Adds a List of frames to the sequence.

        Args:
            frames (list): A List of frames to add to the sequence.
        """
        # Add the frames
        self._frames.extend(frames)

        # If these were the first frames, call next_frame to set things up
        if self._frame_index == -1:
            self.next_frame()

    def next_frame(self):
        """
        Sets up the next frame of the sequence.
        """
        # If there are no frames, we can't do anything here.
        if len(self._frames) == 0: return

        # Increment wrapping around to the beginning.
        self._frame_index += 1
        if (self._frame_index >= len(self._frames)):
            self._frame_index = 0

        # Get the new frame data
        self._frame = self._frames[self._frame_index]
