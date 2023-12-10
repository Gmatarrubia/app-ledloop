#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./ledloop.py

import os
import time
from figuresDict import FiguresDict
from globals import *

def main():

    led_map_json = load_map_json()
    figuresDict = FiguresDict(led_map_json)
    myFigures = figuresDict.figuresDict

    def update_mode_work():
        print("Updating mode work...")
        # Read new json values
        work_mode_json = load_mode_json()
        myFigures["complete"].mode(work_mode_json["complete"])
        myFigures["core"].mode(work_mode_json["core"])
        print("Succesfuly mode work updated.")

    def run_figures():
        #Start thread again
        myFigures["complete"].start()
        myFigures["core"].start()

    def switch_on_core():
        myFigures["core"].fill(0,90,20)
        update_all()

    def switch_off_core():
        myFigures["core"].fill(0,0,0)
        update_all()

    # Test led lights
    loop_cycles = 5
    for cycles in range(loop_cycles):
        switch_on_core()
        time.sleep(0.4)
        switch_off_core()
        time.sleep(0.4)

    # Initial mode work
    update_mode_work()
    # Start runnning figures
    run_figures()

    try:
        lastModTime = os.stat(WORK_MODE_JSON_FILE).st_mtime
        currentModTime = lastModTime
        print(str(lastModTime))
        while True:
            time.sleep(0.01)
            currentModTime = os.stat(WORK_MODE_JSON_FILE).st_mtime
            if (currentModTime == lastModTime):
                update_all()
                continue
            time.sleep(0.5)
            lastModTime = currentModTime
            update_mode_work()

    except KeyboardInterrupt:
        # Manually stop all active listener threads if you press Ctrl+C
        print("Program stopped.")

if __name__ == "__main__":
    main()
