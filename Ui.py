from tkinter import *
from Core import Core
import copy



class Ui:

    def initCanvasMap(self, core):
        canvasMap = copy.deepcopy(core.getMatrix())
        for y in range(core.getMatrixHeight()):
            for x in range(core.getMatrixWidth()):


    def onStartClick(self, y, x, it):
        core = Core(x, y, it)
        map = self.initCanvasMap(core)
        canvasMap = copy.deepcopy(map)

        self.__gameWin = Tk("Running")
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
