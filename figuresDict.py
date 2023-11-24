from figureLedLine import FigureLedLine

class FiguresDict():
    def __init__(self, figureLedsLine) -> None:
        self.figuresDict = {}
        for item in figureLedsLine.items():
            self.figuresDict[item[0]] = FigureLedLine(item[1]["ledLinesList"])
