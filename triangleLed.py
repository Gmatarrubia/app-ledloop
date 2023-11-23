import time
from animationHelpers import wheel
from figureLedLine import FigureLedLine

class TriangleLed(FigureLedLine):

    def __init__(self,line1, line2, line3):
        super().__init__([line1, line2, line3])

