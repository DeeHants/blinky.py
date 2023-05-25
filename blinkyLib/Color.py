class Color:
    def __init__(self, r, g, b):
        self._r = int(r)
        self._g = int(g)
        self._b = int(b)

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    def from_hex(hex_value):
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
