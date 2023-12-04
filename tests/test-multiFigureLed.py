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
from figureLedLine import TriangleLed, FigureLedLine
from globals import *

def main():
    # Single line
    line1 = LedLine(tupla_PIXELS_2, 0, 5)

    # Triangle 1
    t1_line1 = LedLine(tupla_PIXELS, 0, 5)
    t1_line2 =LedLine(tupla_PIXELS, 6, 11)
    t1_line3 =LedLine(tupla_PIXELS, 12, 17)
    triangleLed = TriangleLed(t1_line1, t1_line2, t1_line3)

    # Triangle 2
    t2_line1 = LedLine(tupla_PIXELS_2, 6, 11)
    t2_line2 = LedLine(tupla_PIXELS_2, 12, 17)
    t2_line3 = LedLine(tupla_PIXELS_2, 18, 23)
    triangleLed_2 = TriangleLed(t2_line1, t2_line2, t2_line3)

    # Multi poligon
    poly = FigureLedLine([line1, triangleLed, triangleLed_2])

    num_loop_cycles = 10
    while (num_loop_cycles):
        poly.fill(0,0,100)
        update_all()
        time.sleep(0.1)

        poly.fill(100,0,0)
        update_all()
        time.sleep(0.1)

        num_loop_cycles = num_loop_cycles - 1

if __name__ == "__main__":
    main()
