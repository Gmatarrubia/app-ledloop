#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./ledloop.py

import os
import time
from figuresDict import FiguresDict
import globals as gls

def main():

    led_map_json = gls.load_map_json()
    figuresDict = FiguresDict(led_map_json)
    myFigures = figuresDict.figuresDict

    def update_mode_work():
        print("Updating mode work...")
        # Switch off all pixels
        for pixel in gls.pixelSceneList:
            pixel.fill((0,0,0))
        gls.update_all()
        # Set default mode for all figures
        for figure in myFigures.items():
            myFigures[figure[0]].mode({"name": "default"})
        # Read new json values
        work_mode_json = gls.load_mode_json()
        # Apply new modes
        for figure in work_mode_json.items():
            myFigures[figure[0]].mode(work_mode_json[figure[0]])
        print("Succesfuly mode work updated.")

    def run_figures():
        # Start animation thread
        for figure in myFigures.items():
            myFigures[figure[0]].start()
        print("Figures running!")

    def switch_lights(onOff):
        color = (0,90,20) if onOff else (0,0,0)
        for figure in myFigures.items():
            myFigures[figure[0]].fill(color[0], color[1], color[2])
        gls.update_all()

    # Welcome led lights
    loop_cycles = 10
    for cycle in range(loop_cycles):
        switch_lights(cycle % 2)
        time.sleep(0.4)

    # Initial mode work
    update_mode_work()
    # Start runnning figures
    run_figures()
    # Start update_all() thread
    # FPS = 50 -> 1/50 = 0.02
    gls.run_update_all_thread(0.02)


    try:
        lastModTime = os.stat(gls.WORK_MODE_JSON_FILE).st_mtime
        currentModTime = lastModTime
        while True:
            currentModTime = os.stat(gls.WORK_MODE_JSON_FILE).st_mtime
            if (currentModTime == lastModTime):
                time.sleep(0.5)
                continue
            time.sleep(0.5)
            lastModTime = currentModTime
            update_mode_work()

    except KeyboardInterrupt:
        # Manually stop all active listener threads if you press Ctrl+C
        print("Program stopped.")

if __name__ == "__main__":
    main()
