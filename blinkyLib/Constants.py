__copyright__ = "Copyright Earl Software"
__license__ = "This source code is subject to the BSD 3-Clause license. See Licence.txt for the full licence."
__author__ = "Deanna Earley"


class Consts:
    DEFAULT_LED_COUNT: int = 60

    # Not constant, but needs to be in an early module with no dependencies
    _lastLedCount: int = DEFAULT_LED_COUNT
