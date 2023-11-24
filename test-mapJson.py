#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./test-mapJson.py

import time
from figureLedLine import FigureLedLine
from globals import *

def main():
    json_data = load_json()
    poly = FigureLedLine(json_data["ledLinesList"])

    num_loop_cycles = 10
    while (num_loop_cycles):
        for item in poly.ledLinesList:
            poly.fill(0,0,0)
            item.fill(50,50,50)
            update_all()
            time.sleep(0.4)

        num_loop_cycles = num_loop_cycles - 1
    poly.fill(50,50,50)
    update_all()


if __name__ == "__main__":
    main()
