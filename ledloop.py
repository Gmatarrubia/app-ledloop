#!/usr/bin/python3

# python3 -m debugpy --listen 192.168.1.43:5678 --wait-for-client ./ledloop.py

import time
import threading
from figuresDict import FiguresDict
from globals import *


def config_thread(target_function, event):
    target_args = [event]
    thread = threading.Thread(target=target_function, args=(target_args))
    thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits
    return thread

def main():

    led_map_json = load_map_json()
    work_mode_json = load_mode_json()
    figuresDict = FiguresDict(led_map_json)
    myFigures = figuresDict.figuresDict

    # Start with last configuraton (from json)
    myFigures["complete"].mode(work_mode_json["complete"])
    myFigures["core"].mode(work_mode_json["core"])
    update_all()

    def switch_on_core():
        myFigures["core"].fill(0,90,20)
        update_all()

    def switch_off_core():
        myFigures["core"].fill(0,0,0)
        update_all()


    # Change sequence event (aka killing event)
    #change_sec = threading.Event()

    #leds_thread = config_thread(switch_off_core, change_sec)

    # Test de luces
    loop_cycles = 5
    for cycles in range(loop_cycles):
        switch_on_core()
        time.sleep(1)
        switch_off_core()
        time.sleep(1)

    try:
        while True:
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Manually stop all active listener threads if you press Ctrl+C
        print("Program stopped.")

if __name__ == "__main__":
    main()