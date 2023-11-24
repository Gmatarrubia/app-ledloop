import time
from animationHelpers import wheel
from ledLine import LedLine
from globals import *

class FigureLedLine():

    def __init__(self, ledLineList):
        self.ledLinesList = []
        for item in ledLineList:
            if isinstance(item, dict):
            # This is True when the info comes from a json file
                if "ledLinesList" in item.keys():
                    self.ledLinesList.append(FigureLedLine(item["ledLinesList"]))
                else:
                    my_tupla = (item["pixel"], pixelSceneDict[item["pixel"]])
                    self.ledLinesList.append(LedLine(my_tupla, item["first"], item["last"]))
                continue
            # Direct append for non json info
            self.ledLinesList.append(item)
        self.lenght = len(self.ledLinesList)

    def fill(self, r, g, b):
        for line in self.ledLinesList:
            line.fill(r, g, b)

    def off(self):
        for line in self.ledLinesList:
            line.fill(0, 0, 0)

    def rainbow(self, wait):
        for line in self.ledLinesList:
            line.rainbow()
            time.sleep(wait)

    def show(self):
        for line in self.ledLinesList:
            line.neopixel.show()

class TriangleLed(FigureLedLine):

    def __init__(self,line1, line2, line3):
        super().__init__([line1, line2, line3])

class SquareLed(FigureLedLine):

    def __init__(self,line1, line2, line3, line4):
        super().__init__([line1, line2, line3, line4])


class HexagonLed(FigureLedLine):

    def __init__(self,line1, line2, line3, line4, line5, line6):
        super().__init__([line1, line2, line3, line4, line5, line6])

