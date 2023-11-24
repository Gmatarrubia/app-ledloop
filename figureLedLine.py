import time
from enum import IntEnum
from animationHelpers import wheel
from ledLine import LedLine
from globals import *

class Figure(IntEnum):
    Triangle = 3
    Square = 4
    Hexagon = 6

class FigureLedLine():

    def __init__(self, ledLineList):
        self.ledLinesList = []
        for item in ledLineList:
            if isinstance(item, dict):
            # This is True when the info comes from a json file

                if "ledLinesList" in item.keys():
                # This is True when the item is another figure,
                # otherwise it is a single Ledline
                    match len(item["ledLinesList"]):
                        case Figure.Triangle.value:
                            self.ledLinesList.append(TriangleLed(*item["ledLinesList"]))
                        case Figure.Square.value:
                            self.ledLinesList.append(SquareLed(*item["ledLinesList"]))
                        case Figure.Hexagon.value:
                            self.ledLinesList.append(HexagonLed(*item["ledLinesList"]))
                        case _:
                            self.ledLinesList.append(FigureLedLine(*item["ledLinesList"]))
                else:
                # The item is single Ledline
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
    def __init__(self,*args):
        if len(args) != 3:
                raise Exception("Triangle must have 3 elements")
        super().__init__(args)

class SquareLed(FigureLedLine):
    def __init__(self,*args):
        if len(args) != 4:
                raise Exception("Triangle must have 3 elements")
        super().__init__(args)


class HexagonLed(FigureLedLine):
    def __init__(self,*args):
        if len(args) != 6:
                raise Exception("Triangle must have 3 elements")
        super().__init__(args)

