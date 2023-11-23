#!/usr/bin/python3
# For remote debugging use the following command on target device
# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-ledLine.py

import time
import board
import neopixel
from ledLine import LedLine

# Global configuration
LED_DATA_PIN = board.D10
LED_DATA_PIN2 = board.D18
COUNT_LED = 18
COUNT_LED2 = 24
ORDER = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=ORDER, brightness=BRIGHTNESS)
PIXELS_2 = neopixel.NeoPixel(LED_DATA_PIN2, COUNT_LED, pixel_order=ORDER, brightness=BRIGHTNESS)

def main():
    leds = LedLine(PIXELS, 0, 5)
    leds2 =LedLine(PIXELS, 6, 11)
    leds3 =LedLine(PIXELS, 12, 17)
    print(" Led segment lenght: {}".format(str(leds.lenght)))

    num_loop_cycles = 3
    while (num_loop_cycles):
        leds.fill(70,0,0)
        leds2.off()
        leds3.off()
        PIXELS.show()
        time.sleep(0.5)
        leds2.fill(70,70,0)
        leds.off()
        leds3.off()
        PIXELS.show()
        time.sleep(0.5)
        leds3.fill(70,70,70)
        leds.off()
        leds2.off()
        PIXELS.show()
        time.sleep(0.5)
        num_loop_cycles = num_loop_cycles - 1

    leds.rainbow(0.001)
    leds2.rainbow(0.001)
    leds3.rainbow(0.001)

if __name__ == "__main__":
    main()