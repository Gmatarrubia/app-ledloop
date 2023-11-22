
class ledSegment():

    def __init__(self, neopixel,first, last):
        self.pixel = neopixel
        self.first = first
        self.last = last
        self.lenght = len(range(first, last))

    def fill(self, r, g, b):
        for led in range(self.first, self.last):
            self.pixel[led] = (r, g, b)

    def off(self):
        self.fill(0, 0, 0)

    def show(self):
        self.pixel.show()