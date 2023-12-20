import time
import threading
from animationHelpers import wheel
from ledLine import LedLine
import globals as gls

class FigureLedLine(threading.Thread):

    def __init__(self, ledLineList):
        self.ledLinesList = []
        self.indexPlain = []
        self.figureName = ledLineList["name"]
        self.activeMode = {"name" : "default"}
        for item in ledLineList["ledLinesList"]:
            if isinstance(item, dict):
            # This is True when the info comes from a json file
                # The item is single Ledline
                my_tupla = (item["pixel"], gls.pixelSceneDict[item["pixel"]])
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
        self.getIndexPlain()

    def getIndexPlain(self):
        for line in self.ledLinesList:
            for num in line.index:
                counter = 0
                self.indexPlain.append((counter, num, line, line.key))
                counter = counter + 1
        return

    def getColorFromArg(self, numArg):
        if "r" in self.activeMode["args"][numArg]:
            r = self.activeMode["args"][numArg]["r"]
            g = self.activeMode["args"][numArg]["g"]
            b = self.activeMode["args"][numArg]["b"]
            return (r, g, b)
        else:
            return (100,100,100)

    def getDoubleFromArg(self, numArg):
        if "value" in self.activeMode["args"][numArg]:
            return self.activeMode["args"][numArg]["value"]
        else:
            return 0.5


    ### Mode's functions at figures level ###

    def fill(self, r, g, b):
        for line in self.ledLinesList:
            line.fill(r, g, b)

    def off(self):
        self.fill(0,0,0)

    def snake(self):
        r, g, b = self.getColorFromArg(0)
        wait = self.getDoubleFromArg(1)
        for pix in self.indexPlain:
            self.off()
            pix[2].neopixel[pix[1]] = (r, g, b)
            time.sleep(wait)
        for pix in reversed(self.indexPlain):
            self.off()
            pix[2].neopixel[pix[1]] = (r, g, b)
            time.sleep(wait)

    def rainbow(self, wait, active_wheel):
        active_wheel = 1 if active_wheel else 0
        for j in range(255):
            for pix in self.indexPlain:
                pixel_index = (pix[active_wheel] * 256 // len(self.indexPlain)) + j
                pix[2].neopixel[pix[1]] = wheel(pix[2].neopixel.byteorder, pixel_index & 255)
            time.sleep(wait)

    def pulse(self):
        r, g, b = self.getColorFromArg(0)
        wait = self.getDoubleFromArg(1)
        long = self.ledLinesList[0].lenght
        for led in range(long):
            self.off()
            for line in self.ledLinesList:
                line.setLed(led, r, g, b)
            time.sleep(wait)
        self.off()
        time.sleep(wait*5)

    def christmas(self):
        long = len(self.indexPlain)
        ledList = list(range(0, long, 6))
        for color in range(3):
            self.off()
            for n in range (0, 5, 2):
                for num in ledList:
                    self.indexPlain[num+n][2].neopixel[self.indexPlain[num+n][1]] = self.getColorFromArg(color)
                time.sleep(0.5)

    def show(self):
        for line in self.ledLinesList:
            line.neopixel.show()

    def mode(self, work_mode):
        self.activeMode = work_mode

    ### Thread main loop ###
    def run(self):
        while True:
            match self.activeMode["name"]:
                case "fill":
                    color = self.getColorFromArg(0)
                    self.fill(*color)
                    time.sleep(0.45)
                case "off":
                    self.off()
                    time.sleep(0.45)
                case "rainbow":
                    self.rainbow(0.005, 0)
                case "rainbow_wheel":
                    self.rainbow(0.005, 1)
                case "snake":
                    self.snake()
                case "pulse":
                    self.pulse()
                case "christmas":
                    self.christmas()
                case _:
                    time.sleep(0.45)


