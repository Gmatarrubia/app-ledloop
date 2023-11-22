
class ledSegment():

    def __init__(self, neopixel, leds):
        self.pixel = neopixel
        self.leds = leds
        self.num = len(leds)

    def fill(self, r, g, b):
        for led in self.leds:
            led = (r, g, b)

    def off(self):
        self._fill(0, 0, 0)
        self.pixel.show()

