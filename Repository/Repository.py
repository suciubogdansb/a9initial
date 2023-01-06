from copy import deepcopy

from Entities.constants import ROWS, COLUMNS


class Board:
    def __init__(self):
        self.__board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    def getBoard(self):
        return self.__board

    def setBoard(self, newBoard):
        self.__board = deepcopy(newBoard)

    def addPiece(self, piece):
        self.__board[piece.row][piece.column] = piece