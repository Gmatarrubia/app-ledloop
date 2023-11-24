#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-mapJson.py

import time
from figuresDict import FiguresDict
from globals import *

def main():
    led_map_json = load_map_json()
    work_mode_json = load_mode_json()
    figuresDict = FiguresDict(led_map_json)
    myFigures = figuresDict.figuresDict

    num_loop_cycles = 13
    while (num_loop_cycles):
        for figure in myFigures.items():
            figure[1].fill(50,0,50)
            update_all()
            time.sleep(0.4)

        num_loop_cycles = num_loop_cycles - 1

    myFigures["core"].fill(0,90,20)
    update_all()


if __name__ == "__main__":
    main()

