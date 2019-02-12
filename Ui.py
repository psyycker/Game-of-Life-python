from tkinter import *
from Core import Core
import copy



class Ui:

    def initCanvasMap(self, core, canvas):
        canvasMap = copy.deepcopy(core.getMatrix())
        for y in range(core.getMatrixHeight()):
            for x in range(core.getMatrixWidth()):
                if core.getValueAtPosition(y, x) == 0:
                    canvasMap[y][x] = canvas.create_rectangle((400 / 40), (400 / 40), y * (400 / 40), x * (400 / 40), fill="black")
                else:
                    canvasMap[y][x] = canvas.create_rectangle((400 / 40), (400 / 40), y * (400 / 40), x * (400 / 40), fill="white")
        return canvasMap

    def onStartClick(self, y, x, it):
        self.__gameWin = Tk("Running")
        core = Core(x, y, it)
        canvas = Canvas(self.__gameWin, width=200, height=200)
        map = self.initCanvasMap(core, canvas)
        canvas.pack()
        for index in range(it):

            self.__gameWin.update_idletasks()
            self.__gameWin.update()
        self.__gameWin.mainloop()

    def __init__(self):
        print("the ui")
        self.__masterWin = Tk("Game of Life")
        startButton = Button(self.__masterWin, text="Start", command=lambda: self.onStartClick(40, 40, 1000))
        startButton.pack()
        mainloop()
