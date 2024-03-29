import neopixel
from math import sin, pi

def shiftPosition(lenght, pos, delta):
    newPos = pos + delta
    if newPos >= lenght:
        newPos = newPos - lenght
    return newPos

def wave_factor(lenght, pos):
    degrees = 180 * pos / lenght
    radians = degrees * ( pi / 180.0 )
    return sin(radians)

def wheel(order, pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if order in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
