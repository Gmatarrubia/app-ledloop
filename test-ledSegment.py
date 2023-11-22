import time
import board
import neopixel
import ledSegment from ledSegment

# Global configuration
LED_DATA_PIN = board.D10
LED_DATA_PIN2 = board.D18
COUNT_LED = 24
COUNT_LED2 = 24
ORDER = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=ORDER, brightness=BRIGHTNESS)
PIXELS_2 = neopixel.NeoPixel(LED_DATA_PIN2, COUNT_LED, pixel_order=ORDER, brightness=BRIGHTNESS)

def main():
    ledSegment(PIXELS, PIXELS[0:5])
    print(" Led segment lenght: {}" % ledSegment.num)

    num_loop_cycles = 10
    while (num_loop_cycles):
        ledSegment.fill(70,0,0)
        time.sleep(1)
        ledSegment.off()
        time.sleep(1)
        num_loop_cycles = num_loop_cycles - 1

if __name__ == main:
    main()
