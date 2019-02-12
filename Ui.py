from tkinter import *
from Core import Core
import copy
import os



class Ui:

    def initCanvasMap(self, core, canvas):
        sizeX = core.getMatrixWidth()
        sizeY = core.getMatrixHeight()
        canvasMap = copy.deepcopy(core.getMatrix())
        for y in range(core.getMatrixHeight()):
            for x in range(core.getMatrixWidth()):
                leftX = x * (self.WinX / sizeX)
                rightX = leftX + (self.WinX / sizeX)
                topY = y * (self.WinY / sizeY)
                botY = topY + (self.WinY / sizeY)
                if core.getValueAtPosition(y, x) == 0:
                    canvasMap[y][x] = canvas.create_rectangle(leftX, topY, rightX, botY, fill="black")
                else:
                    canvasMap[y][x] = canvas.create_rectangle(leftX, topY, rightX, botY, fill="white")
        return canvasMap

    def updateCanvasMap(self, core, canvasMap, canvas):
        for y in range(core.getMatrixHeight()):
            for x in range(core.getMatrixWidth()):
                if core.getValueAtPosition(y, x)== 1:
                    coul = "white"
                else:
                    coul = "black"
                canvas.itemconfig(canvasMap[y][x], fill=coul)

        return canvasMap

    def onStartClick(self, y, x, it):
        self.__gameWin = Tk("Running")
        core = Core(x, y, it)
        canvas = Canvas(self.__gameWin, width=self.WinX, height=self.WinY, background="black")
        map = self.initCanvasMap(core, canvas)
        canvas.pack()
        for index in range(it):
            core.iterate()
            self.updateCanvasMap(core, map, canvas)
            self.__gameWin.update_idletasks()
            self.__gameWin.update()
        self.__gameWin.mainloop()

    def onSpecificStartClick(self, filename, it):
        self.__gameWin = Tk("Running")
        confFile = open("confs/" + filename + ".txt", 'r')
        result = confFile.read()
        core = Core(0 ,0, it)
        core.genFromText(result)
        canvas = Canvas(self.__gameWin, width=self.WinX, height=self.WinY, background="black")
        map = self.initCanvasMap(core, canvas)
        canvas.pack()
        for index in range(it):
            core.iterate()
            self.updateCanvasMap(core, map, canvas)
            self.__gameWin.update_idletasks()
            self.__gameWin.update()
        self.__gameWin.mainloop()


    def genListBox(self, listbox):
        files = os.listdir("confs")
        for name in files:
            listbox.insert(END, name.replace(".txt", ""))

    def __init__(self):
        self.WinX = 800
        self.WinY = 800
        self.__masterWin = Tk("Game of Life")
        x = Entry(self.__masterWin)
        x.pack()
        y = Entry(self.__masterWin)
        y.pack()
        startButton = Button(self.__masterWin, text='Start', command=lambda: self.onStartClick(int(y.get()), int(x.get()), 1000))
        startButton.pack(side=LEFT, padx=5, pady=5)
        listbox = Listbox(self.__masterWin)
        listbox.pack()
        self.genListBox(listbox)
        specificButton = Button(self.__masterWin, text='10 Cells', command=lambda: self.onSpecificStartClick(listbox.get(ACTIVE), 1000))
        specificButton.pack(side=LEFT, padx=5, pady=5)
        self.__masterWin.lift()
        self.__masterWin.attributes('-topmost', True)
        self.__masterWin.update_idletasks()
        self.__masterWin.update()
        mainloop()
