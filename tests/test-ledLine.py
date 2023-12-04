#!/usr/bin/python3
# For remote debugging use the following command on target device
# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-ledLine.py

import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from ledLine import LedLine
from globals import *

def main():
    leds1 = LedLine(tupla_PIXELS, 0, 5)
    leds2 = LedLine(tupla_PIXELS, 6, 11)
    leds3 = LedLine(tupla_PIXELS, 12, 17)
    print(" Led segment lenght: {}".format(str(leds1.lenght)))

    num_loop_cycles = 3
    while (num_loop_cycles):
        leds1.fill(70,0,0)
        leds2.off()
        leds3.off()
        PIXELS.show()
        time.sleep(0.5)
        leds2.fill(70,70,0)
        leds1.off()
        leds3.off()
        PIXELS.show()
        time.sleep(0.5)
        leds3.fill(70,70,70)
        leds1.off()
        leds2.off()
        PIXELS.show()
        time.sleep(0.5)
        num_loop_cycles = num_loop_cycles - 1

    leds1.rainbow(0.001)
    leds2.rainbow(0.001)
    leds3.rainbow(0.001)

if __name__ == "__main__":
    main()
