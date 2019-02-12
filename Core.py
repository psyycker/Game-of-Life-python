import random

class Core:
    def __init__(self, cols, rows, it):
        self.__cols = cols
        self.__rows = rows
        self.__it = it
        self.__matrix = [[0 for x in range(self.__cols)] for y in range(self.__rows)]
        self.generateMap()
        self.__debug = False

    def setDebug(self, debug):
        self.__debug = debug

    def debugPrint(self, value):
        if self.__debug:
            print(value)

    def generateMap(self):
        for y in range(self.getMatrixHeight()):
            for x in range(self.getMatrixWidth()):
                self.__matrix[y][x] = random.randint(0, 1)

    def getIterationsLeft(self):
        return self.__it

    def getMatrixWidth(self):
        return len(self.__matrix[0])

    def getMatrixHeight(self):
        return len(self.__matrix)

    def getValueAtPosition(self, y, x):
        return self.__matrix[y][x]

    def setValueAtPosition(self, y, x, value):
        self.__matrix[y][x] = value

    def getLivingCellsCount(self):
        counter = 0
        for y in range(self.getMatrixHeight()):
            for x in range(self.getMatrixWidth()):
                if self.getValueAtPosition(y, x) == 1:
                    counter = counter + 1
        return counter

    def getDeadCellsCount(self):
        counter = 0
        for y in range(self.getMatrixHeight()):
            for x in range(self.getMatrixWidth()):
                if self.getValueAtPosition(y, x) == 0:
                    counter = counter + 1
        return counter

    def getLeftCell(self, y, x):
        tempX = x - 1
        if tempX < 0:
            return 0
        return self.getValueAtPosition(y, tempX)

    def getRightCell(self, y, x):
        tempX = x + 1
        if tempX > self.getMatrixWidth() - 1:
            return 0
        return self.getValueAtPosition(y, tempX)

    def getTopCell(self, y, x):
        tempY = y - 1
        if tempY < 0:
            return 0
        return self.getValueAtPosition(tempY, x)

    def getBottomCell(self, y, x):
        tempY = y + 1
        if tempY > self.getMatrixHeight() - 1:
            return 0
        return self.getValueAtPosition(tempY, x)

    def getTopLeftCell(self, y, x):
        tempY = y - 1
        tempX = x - 1
        if tempY < 0 or tempX < 0:
            return 0
        return self.getValueAtPosition(tempY, tempX)

    def getTopRightCell(self, y, x):
        tempY = y - 1
        tempX = x + 1
        if tempY < 0 or tempX > self.getMatrixWidth() - 1:
            return 0
        return self.getValueAtPosition(tempY, tempX)

    def getBottomLeftCell(self, y, x):
        tempY = y + 1
        tempX = x - 1
        if tempY > self.getMatrixHeight() - 1 or tempX < 0:
            return 0
        return self.getValueAtPosition(tempY, tempX)

    def getBottomRightCell(self, y, x):
        tempY = y + 1
        tempX = x + 1
        if tempY > self.getMatrixHeight() - 1 or tempX > self.getMatrixWidth() - 1:
            return 0
        return self.getValueAtPosition(tempY, tempX)

    def computeValue(self, y, x, counter):
        currentValue = self.getValueAtPosition(y, x)
        if currentValue is 0:
            if counter == 3:
                self.debugPrint("Reproduction")
                self.setValueAtPosition(y, x, 1)
        else:
            if counter > 3:
                self.debugPrint("Overpopulation")
                self.setValueAtPosition(y, x, 0)
            elif counter == 2 or counter == 3:
                self.debugPrint("Stasis")
                # self.setValueAtPosition(y, x, 1)
            elif counter < 2:
                self.debugPrint("Underpopulation")
                self.setValueAtPosition(y, x, 0)

    def iterate(self):
        if self.__it is 0:
            return False
        for y in range(self.getMatrixHeight()):
            for x in range(self.getMatrixWidth()):
                counter = self.getLeftCell(y, x)
                counter += self.getRightCell(y, x)
                counter += self.getTopCell(y, x)
                counter += self.getBottomCell(y, x)
                counter += self.getTopLeftCell(y, x)
                counter += self.getTopRightCell(y, x)
                counter += self.getBottomLeftCell(y, x)
                counter += self.getBottomRightCell(y, x)
                self.computeValue(y, x, counter)
        self.__it = self.__it - 1
        return True


