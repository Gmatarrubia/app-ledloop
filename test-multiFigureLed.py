#!/usr/bin/python3
# For remote debugging use the following command on target device
# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-ledSegment.py

import time
import board
import neopixel
from ledLine import LedLine
from figureLedLine import TriangleLed, FigureLedLine

# Global configuration
LED_DATA_PIN = board.D10
LED_DATA_PIN2 = board.D18
COUNT_LED = 18
COUNT_LED2 = 24
RGB = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=RGB, brightness=BRIGHTNESS, auto_write=False)
PIXELS_2 = neopixel.NeoPixel(LED_DATA_PIN2, COUNT_LED2, pixel_order=RGB, brightness=BRIGHTNESS, auto_write=False)

pixelScene = []
pixelScene.append(PIXELS)
pixelScene.append(PIXELS_2)

def update_scene(pixelList):
    for pixel in pixelList:
        pixel.show()

def main():
    # Single line
    line1 = LedLine(PIXELS_2, 0, 5)

    # Triangle 1
    t1_line1 = LedLine(PIXELS, 0, 5)
    t1_line2 =LedLine(PIXELS, 6, 11)
    t1_line3 =LedLine(PIXELS, 12, 17)
    triangleLed = TriangleLed(t1_line1, t1_line2, t1_line3)

    # Triangle 2
    t2_line1 = LedLine(PIXELS_2, 6, 11)
    t2_line2 = LedLine(PIXELS_2, 12, 17)
    t2_line3 = LedLine(PIXELS_2, 18, 23)
    triangleLed_2 = TriangleLed(t2_line1, t2_line2, t2_line3)

    # Multi poligon
    poly = FigureLedLine([line1, triangleLed, triangleLed_2])

    num_loop_cycles = 10
    while (num_loop_cycles):
        poly.fill(0,0,100)
        update_scene(pixelScene)
        time.sleep(0.1)

        poly.fill(100,0,0)
        update_scene(pixelScene)
        time.sleep(0.1)

        num_loop_cycles = num_loop_cycles - 1

if __name__ == "__main__":
    main()
