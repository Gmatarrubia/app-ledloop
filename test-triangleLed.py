#!/usr/bin/python3
# For remote debugging use the following command on target device
# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-ledSegment.py

import time
import board
import neopixel
from ledLine import LedLine
from triangleLed import TriangleLed

# Global configuration
LED_DATA_PIN = board.D10
LED_DATA_PIN2 = board.D18
COUNT_LED = 18
COUNT_LED2 = 24
RGB = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=RGB, brightness=BRIGHTNESS)
PIXELS_2 = neopixel.NeoPixel(LED_DATA_PIN2, COUNT_LED2, pixel_order=RGB, brightness=BRIGHTNESS)

pixelScene = []
pixelScene.append(PIXELS)
pixelScene.append(PIXELS_2)

def update_scene(pixelList):
    for pixel in pixelList:
        pixel.show()

def main():
    leds = LedLine(PIXELS, 0, 5)
    leds2 =LedLine(PIXELS, 6, 11)
    leds3 =LedLine(PIXELS, 12, 17)
    triangleLed = TriangleLed(leds, leds2, leds3)

    t2_line1 = LedLine(PIXELS_2, 6, 11)
    t2_line2 = LedLine(PIXELS_2, 12, 17)
    t2_line3 = LedLine(PIXELS_2, 18, 23)
    triangleLed_2 = TriangleLed(t2_line1, t2_line2, t2_line3)

    num_loop_cycles = 10
    while (num_loop_cycles):
        triangleLed.fill(0,0,100)
        triangleLed_2.fill(100,0,0)
        update_scene(pixelScene)
        time.sleep(0.1)

        triangleLed.fill(100,0,0)
        triangleLed_2.fill(0,0,100)
        update_scene(pixelScene)
        time.sleep(0.1)

        num_loop_cycles = num_loop_cycles - 1

if __name__ == "__main__":
    main()
