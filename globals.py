import json
import board
import neopixel

# Global configuration
LED_DATA_PIN = board.D10
LED_DATA_PIN2 = board.D18
COUNT_LED = 18
COUNT_LED2 = 24
RGB = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=RGB, brightness=BRIGHTNESS, auto_write=False)
PIXELS_2 = neopixel.NeoPixel(LED_DATA_PIN2, COUNT_LED2, pixel_order=RGB, brightness=BRIGHTNESS, auto_write=False)

tupla_PIXELS = ("PIXELS", PIXELS)
tupla_PIXELS_2 = ("PIXELS_2", PIXELS_2)

pixelSceneDict = {}
pixelSceneDict["PIXELS"] = PIXELS
pixelSceneDict["PIXELS_2"] = PIXELS_2

pixelSceneList = []
pixelSceneList.append(PIXELS)
pixelSceneList.append(PIXELS_2)

def update_all():
    for pixel in pixelSceneList:
        pixel.show()

# Json utils
MAP_JSON_FILE = "led-map.json"
WORK_MODE_JSON_FILE = "work-mode.json"
def load_map_json():
    with open(MAP_JSON_FILE, "r") as f:
        return json.load(f)
def load_mode_json():
    with open(WORK_MODE_JSON_FILE, "r") as f:
        return json.load(f)
