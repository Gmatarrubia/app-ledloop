import time
from animationHelpers import wheel

class LedLine():

    def __init__(self, tupla_neopixel,first, last, reverse=False):
        self.key, self.neopixel = tupla_neopixel
        self.first = first
        self.last = last
        self.index = [*range(self.first, self.last + 1)]
        self.lenght = len(self.index)
        if reverse:
            self.index = [*reversed(self.index)]

    def fill(self, r, g, b):
        for led in self.index:
            self.neopixel[led] = (r, g, b)

    def off(self):
        self.fill(0, 0, 0)

    def rainbow(self, wait):
        for j in range(255):
            for i in self.index:
                pixel_index = (i * 256 // self.lenght) + j
                self.neopixel[i] = wheel(self.neopixel.byteorder, pixel_index & 255)
            self.show()
            time.sleep(wait)

    def show(self):
        self.neopixel.show()