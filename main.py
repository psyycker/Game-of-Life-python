from Core import Core

def main():
    print("Starting Game of Life")
    coreInst = Core(40, 40, 100)
    coreInst.setDebug(False)

    while coreInst.iterate() is True:
        pass
    print(coreInst.getLivingCellsCount())
    print(coreInst.getDeadCellsCount())


if __name__ == '__main__':
    main()
