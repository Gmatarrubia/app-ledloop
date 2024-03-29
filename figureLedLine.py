import time
import threading
import random
from animationHelpers import wheel, shiftPosition
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

    def pang(self):
        color = self.getColorFromArg(0)
        background_color = self.getColorFromArg(1)
        wait = 1.00/self.getDoubleFromArg(2)
        for pix in self.indexPlain:
            self.fill(*background_color)
            pix[2].neopixel[pix[1]] = color
            time.sleep(wait)
        for pix in reversed(self.indexPlain):
            self.fill(*background_color)
            pix[2].neopixel[pix[1]] = color
            time.sleep(wait)

    def rainbow(self, wait, active_wheel):
        active_wheel = 1 if active_wheel else 0
        for j in range(255):
            for pix in self.indexPlain:
                pixel_index = (pix[active_wheel] * 256 // len(self.indexPlain)) + j
                pix[2].neopixel[pix[1]] = wheel(pix[2].neopixel.byteorder, pixel_index & 255)
            time.sleep(wait)

    def pulse(self):
        color = self.getColorFromArg(0)
        background_color = self.getColorFromArg(1)
        wait = 1.00/self.getDoubleFromArg(2)
        long = self.ledLinesList[0].lenght
        for led in range(long):
            self.fill(*background_color)
            for line in self.ledLinesList:
                line.setLed(led, *color)
            time.sleep(wait)
        self.fill(*background_color)
        time.sleep(wait*5)

    def pulse_fill_in_out(self):
        color = self.getColorFromArg(0)
        background_color = self.getColorFromArg(1)
        out_mode = self.getDoubleFromArg(2)
        wait = 1.00/self.getDoubleFromArg(3)
        long = self.ledLinesList[0].lenght
        for led in range(long):
            for line in self.ledLinesList:
                line.setLed(led, *color)
            time.sleep(wait)
        fade_out_list = range(long) if out_mode == 0 else reversed(range(long))
        for led in fade_out_list:
            for line in self.ledLinesList:
                line.setLed(led, *background_color)
            time.sleep(wait)
        self.fill(*background_color)
        time.sleep(wait*5)

    def breathing(self):
        color = self.getColorFromArg(0)
        wait = self.getDoubleFromArg(1)
        finalColor = ""
        for factor in range(20):
            finalColor = tuple(int(x * (factor/20.0)) for x in color)
            self.fill(*finalColor)
            time.sleep(wait)
        for factor in reversed(range(20)):
            finalColor = tuple(int(x * (factor/20.0)) for x in color)
            self.fill(*finalColor)
            time.sleep(wait)
        time.sleep(0.2)

    def bicolor(self):
        color1 = self.getColorFromArg(0)
        color2 = self.getColorFromArg(1)
        lenght = int(self.getDoubleFromArg(2))
        subListCounter = 0
        for subListFirst in range(0, len(self.indexPlain), lenght):
            for counter in range(lenght):
                ledNum = subListFirst+counter
                if subListCounter % 2 == 0:
                    self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = color1
                else:
                    self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = color2
            subListCounter = subListCounter + 1

    def bicolor_wheel(self):
        color1 = self.getColorFromArg(0)
        color2 = self.getColorFromArg(1)
        lenght = int(self.getDoubleFromArg(2))
        wait = self.getDoubleFromArg(3)
        for shifter in range(lenght * 2):
            subListCounter = 0
            for subListFirst in range(0, len(self.indexPlain), lenght):
                for counter in range(lenght):
                    ledNum =  shiftPosition(len(self.indexPlain), subListFirst+counter, shifter)
                    if subListCounter % 2 == 0:
                        self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = color1
                    else:
                        self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = color2
                subListCounter = subListCounter + 1
            time.sleep(wait)

    def fill_in_out(self):
        color = self.getColorFromArg(0)
        revert_mode = self.getDoubleFromArg(1)
        wait = 1/self.getDoubleFromArg(2)
        for pix in self.indexPlain:
            pix[2].neopixel[pix[1]] = color
            time.sleep(wait)
        fade_out_list = self.indexPlain if revert_mode == 0 else reversed(self.indexPlain)
        for pix in fade_out_list:
            pix[2].neopixel[pix[1]] = (0,0,0)
            time.sleep(wait)

    def christmas(self):
        long = len(self.indexPlain)
        ledList = list(range(0, long, 6))
        for color in range(3):
            self.off()
            for n in range (0, 5, 2):
                for num in ledList:
                    self.indexPlain[num+n][2].neopixel[self.indexPlain[num+n][1]] = self.getColorFromArg(color)
                time.sleep(0.5)

    def glitch(self):
        color = self.getColorFromArg(0)
        glitchLenght = int(self.getDoubleFromArg(1))
        ledsLenght = len(self.indexPlain)
        self.fill(*color)
        firstLed = random.randint(0, ledsLenght)
        for flicker in range(4):
            modColor = (0, 0, 0) if flicker % 2 == 0 else color
            for shifter in range(glitchLenght):
                ledNum =  shiftPosition(ledsLenght, firstLed, shifter)
                self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = modColor
            randomFlicker = random.randint(1, 20)
            time.sleep(randomFlicker/100)
        randomWait = random.randint(5, 20)
        time.sleep(randomWait/10.0)

    def shining_stars(self):
        color = self.getColorFromArg(0)
        ledNum = random.randint(0, len(self.indexPlain)-1)
        finalColor = (0,0,0)
        if self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] == [0,0,0]:
            finalColor = color
        self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = finalColor
        time.sleep(0.02)

    def fire(self):
        fireColors = [[255,0,0],[188,57,0],[200, 200, 0],[0,0,0]]
        ledNum = random.randint(0, len(self.indexPlain)-1)
        finalColorIndex = random.randint(0, len(fireColors)-1)
        self.indexPlain[ledNum][2].neopixel[self.indexPlain[ledNum][1]] = fireColors[finalColorIndex]
        time.sleep(0.02)

    def show(self):
        for line in self.ledLinesList:
            line.neopixel.show()

    def mode(self, work_mode):
        self.activeMode = work_mode

    ### Thread main loop ###
    def run(self):
        while True:
            try:
                match self.activeMode["name"]:
                    case "fill":
                        color = self.getColorFromArg(0)
                        self.fill(*color)
                        time.sleep(0.45)
                    case "off":
                        self.off()
                        time.sleep(0.45)
                    case "bicolor":
                        self.bicolor()
                        time.sleep(0.45)
                    case "bicolor_wheel":
                        self.bicolor_wheel()
                    case "rainbow":
                        self.rainbow(0.005, 0)
                    case "rainbow_wheel":
                        self.rainbow(0.005, 1)
                    case "pang":
                        self.pang()
                    case "pulse":
                        self.pulse()
                    case "pulse_fill_in_out":
                        self.pulse_fill_in_out()
                    case "christmas":
                        self.christmas()
                    case "breathing":
                        self.breathing()
                    case "glitch":
                        self.glitch()
                    case "fill_in_out":
                        self.fill_in_out()
                    case "shining stars":
                        self.shining_stars()
                    case "fire":
                        self.fire()
                    case _:
                        time.sleep(0.45)
            except Exception:
                #print("Exception managed")
                time.sleep(0.45)

