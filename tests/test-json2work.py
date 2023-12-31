#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-json2work.py

import os
import time
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

from figuresDict import FiguresDict
from globals import *

def main():
    led_map_json = load_map_json()
    work_mode_json = load_mode_json()
    figuresDict = FiguresDict(led_map_json)
    myFigures = figuresDict.figuresDict

    for item in work_mode_json.items():
        if item[0] in myFigures.keys():
            myFigures[item[0]].mode(item[1])
            update_all()
            time.sleep(0.4)


if __name__ == "__main__":
    main()

