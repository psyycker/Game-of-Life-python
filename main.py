from Core import Core

def main():
    print("Starting Game of Life")
    coreInst = Core(40, 40, 1000)
    coreInst.setDebug(True)
    coreInst.iterate()
    print(coreInst.getLivingCellsCount())
    print(coreInst.getDeadCellsCount())


if __name__ == '__main__':
    main()
