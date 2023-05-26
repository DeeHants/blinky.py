class Color:
    def __init__(self, r, g, b):
        """
        Initializes a new instance of the Color class.

        Args:
            r (_type_): Red component from 0 to 255.
            g (_type_): Green component from 0 to 255.
            b (_type_): Blue component from 0 to 255.
        """
        self._r = int(r)
        self._g = int(g)
        self._b = int(b)

    @property
    def r(self):
        """Return the color red component."""
        return self._r

    @property
    def g(self):
        """Return the color green component."""
        return self._g

    @property
    def b(self):
        """Return the color blue component."""
        return self._b

    def from_hex(hex_value):
        """
        Return a Color object for a given 24-bit color value.

        Args:
            hex_value (_type_): An integer containing the 24-bit color value.

        Returns:
            _type_: A Color object with the associated red, green, and blue values
        """
        return Color(
            (hex_value & 0x00ff0000) >> 16,
            (hex_value & 0x0000ff00) >> 8,
            (hex_value & 0x000000ff) >> 0
        )

    def Black():
        return Color(0, 0, 0)

    def White():
        return Color(255, 255, 255)

    def Red():
        return Color(255, 0, 0)

    def Green():
        return Color(0, 255, 0)

    def Blue():
        return Color(0, 0, 255)
