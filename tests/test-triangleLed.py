#!/usr/bin/python3
# For remote debugging use the following command on target device
# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-ledSegment.py

import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from ledLine import LedLine
from figureLedLine import TriangleLed
from globals import *

def main():
    leds1 = LedLine(tupla_PIXELS, 0, 5)
    leds2 = LedLine(tupla_PIXELS, 6, 11)
    leds3 = LedLine(tupla_PIXELS, 12, 17)
    triangleLed = TriangleLed(leds1, leds2, leds3)

    t2_line1 = LedLine(tupla_PIXELS_2, 6, 11)
    t2_line2 = LedLine(tupla_PIXELS_2, 12, 17)
    t2_line3 = LedLine(tupla_PIXELS_2, 18, 23)
    triangleLed_2 = TriangleLed(t2_line1, t2_line2, t2_line3)

    num_loop_cycles = 10
    while (num_loop_cycles):
        triangleLed.fill(0,0,100)
        triangleLed_2.fill(100,0,0)
        update_all()
        time.sleep(0.1)

        triangleLed.fill(100,0,0)
        triangleLed_2.fill(0,0,100)
        update_all()
        time.sleep(0.1)

        num_loop_cycles = num_loop_cycles - 1

if __name__ == "__main__":
    main()
