import json
import board
import neopixel
from figureLedLine import FigureLedLine, TriangleLed
from ledLine import LedLine

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
