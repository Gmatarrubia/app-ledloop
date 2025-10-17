import os
import json
import time
import threading
import board
import neopixel

APP_PATH = os.path.dirname(os.path.realpath(__file__))

# Global configuration
LED_DATA_PIN = board.D21   # pin 40 on a raspi zero w
#LED_DATA_PIN2 = board.D18  # pin 12 on a raspi zero w
COUNT_LED = 18
COUNT_LED2 = 24
RGB = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=RGB, brightness=BRIGHTNESS, auto_write=False)
#PIXELS_2 = neopixel.NeoPixel(LED_DATA_PIN2, COUNT_LED2, pixel_order=RGB, brightness=BRIGHTNESS, auto_write=False)

tupla_PIXELS = ("PIXELS", PIXELS)
#tupla_PIXELS_2 = ("PIXELS_2", PIXELS_2)

pixelSceneDict = {}
pixelSceneDict["PIXELS"] = PIXELS
#pixelSceneDict["PIXELS_2"] = PIXELS_2

pixelSceneList = []
pixelSceneList.append(PIXELS)
#pixelSceneList.append(PIXELS_2)

def update_all():
    for pixel in pixelSceneList:
        pixel.show()

def run_update_all_thread(wait):
    def update_all_thread(wait):
        while True:
            update_all()
            time.sleep(wait)
    threadArgs = [wait]
    updateThread = threading.Thread(target=update_all_thread, args=threadArgs)
    updateThread.daemon = True
    updateThread.start()

# Json utils
MAP_JSON_FILE = os.path.join(APP_PATH,"led-map.json")
WORK_MODE_JSON_FILE = os.path.join(APP_PATH,"work-mode.json")
def load_map_json():
    with open(MAP_JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def load_mode_json():
    with open(WORK_MODE_JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
