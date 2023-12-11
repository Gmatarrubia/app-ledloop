import time
import threading
from enum import IntEnum
from animationHelpers import wheel
from ledLine import LedLine
from globals import *

class FigureLedLine(threading.Thread):

    def __init__(self, ledLineList):
        self.ledLinesList = []
        self.indexPlain = []
        self.activeMode = ""
        for item in ledLineList:
            if isinstance(item, dict):
            # This is True when the info comes from a json file
                # The item is single Ledline
                my_tupla = (item["pixel"], pixelSceneDict[item["pixel"]])
                if int(item["first"]) < int(item["last"]):
                    self.ledLinesList.append(LedLine(my_tupla, item["first"], item["last"]))
                else:
                    self.ledLinesList.append(LedLine(my_tupla, item["last"], item["first"], True))
                continue
            # Direct append for non json info
            self.ledLinesList.append(item)
        self.lenght = len(self.ledLinesList)
        threading.Thread.__init__(self)
        threading.Thread.daemon = True
        #self.indexPlain = self.getIndexPlain()
        self.getIndexPlain()

    def getIndexPlain(self):
        for line in self.ledLinesList:
            for num in line.index:
                counter = 0
                self.indexPlain.append((counter, num, line, line.key))
                counter = counter + 1
        return

    def fill(self, r, g, b):
        for line in self.ledLinesList:
            line.fill(r, g, b)

    def off(self):
        self.fill(0,0,0)

    def snake(self, wait):
        for pix in self.indexPlain:
            self.off()
            pix[2].neopixel[pix[1]] = (100,100,100)
            time.sleep(wait)
        for pix in reversed(self.indexPlain):
            self.off()
            pix[2].neopixel[pix[1]] = (100,100,100)
            time.sleep(wait)

    def rainbow(self, wait):
        for j in range(255):
            for pix in self.indexPlain:
                pixel_index = (pix[0] * 256 // len(self.indexPlain)) + j
                pix[2].neopixel[pix[1]] = wheel(pix[2].neopixel.byteorder, pixel_index & 255)
            time.sleep(wait)

    def show(self):
        for line in self.ledLinesList:
            line.neopixel.show()

    def mode(self, work_mode):
        self.activeMode = work_mode

    def run(self):
        while True:
            match self.activeMode["mode"]:
                case "fill":
                    color = (self.activeMode["args"]["r"],
                            self.activeMode["args"]["g"],
                            self.activeMode["args"]["b"])
                    self.fill(*color)
                    time.sleep(0.45)
                case "off":
                    self.off()
                    time.sleep(0.45)
                case "rainbow":
                    self.rainbow(0.001)
                case "snake":
                    self.snake(0.02)
                case _:
                    time.sleep(0.45)


