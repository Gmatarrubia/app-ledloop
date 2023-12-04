#!/usr/bin/python3
# For remote debugging use the following command on target device
# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-multi2mapJson.py

import sys
import os
import time
import json

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from ledLine import LedLine
from figureLedLine import TriangleLed, FigureLedLine
from figuresDict import FiguresDict

from globals import *

class Led_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LedLine):
            return {
                "pixel" : obj.key,
                "first": obj.first,
                "last": obj.last}
        if isinstance(obj, FigureLedLine):
            return {"ledLinesList" : obj.ledLinesList}
        return super().default(obj)

def main():
    # Single line
    line1 = LedLine(tupla_PIXELS_2, 0, 5)
    line1_reverse = LedLine(tupla_PIXELS_2, 0, 5, reverse=True)

    # Triangle 1
    t1_line1 = LedLine(tupla_PIXELS, 0, 5)
    t1_line2 = LedLine(tupla_PIXELS, 6, 11)
    t1_line3 = LedLine(tupla_PIXELS, 12, 17)
    triangleLed = TriangleLed(t1_line1, t1_line2, t1_line3)

    # Triangle 2
    t2_line1 = LedLine(tupla_PIXELS_2, 6, 11)
    t2_line2 = LedLine(tupla_PIXELS_2, 12, 17)
    t2_line3 = LedLine(tupla_PIXELS_2, 18, 23)
    triangleLed_2 = TriangleLed(t2_line1, t2_line2, t2_line3)

    # Multi poligon
    complete = FigureLedLine([line1, triangleLed, triangleLed_2])
    core = FigureLedLine([line1_reverse, t1_line1, t2_line1])
    figureGroups = FiguresDict({
                            "complete" : {
                                "ledLinesList" : [complete],
                            },
                            "core" : {
                                "ledLinesList" : [core],
                            }})

    with open(MAP_JSON_FILE, "w") as json_file:
        json.dump(figureGroups.figuresDict, json_file, indent=2, cls=Led_encoder)


if __name__ == "__main__":
    main()
