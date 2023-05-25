class Color:
    def __init__(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def R(self):
        return self.r

    def G(self):
        return self.g

    def B(self):
        return self.b

    def FromHex(hex_value):
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
