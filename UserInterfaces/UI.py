from time import sleep

from Entities.constants import RED, YELLOW
from Entities.exceptions import InputError, FullColumnError


class UI:
    def __init__(self, game):
        self.__game = game
        self.__runningProgram()

    def __runningProgram(self):
        gameOver = False
        currentPlayer = RED
        while not gameOver:
            try:
                for row in self.__game.getBoard():
                    print(row)
                if currentPlayer == RED:
                    try:
                        inputColumn = int(input("Input 1-7 to choose a column: "))
                        if inputColumn not in range(1, 8):
                            raise ValueError
                    except ValueError:
                        raise InputError("Invalid input")
                    if not self.__game.checkValidColumn(inputColumn-1):
                        raise FullColumnError("The column is full")
                    self.__game.dropPiece(inputColumn-1)
                    if self.__game.checkVictory():
                        print("The player won!")
                        for row in self.__game.getBoard():
                            print(row)
                        gameOver = True
                else:
                    self.__game.aiMove()
                    print()
                    if self.__game.checkVictory():
                        print("The computer won!")
                        for row in self.__game.getBoard():
                            print(row)
                        sleep(2)
                        gameOver = True
                currentPlayer = RED if currentPlayer == YELLOW else YELLOW

            except Exception as e:
                print(e)
                sleep(2)
