from copy import deepcopy

from Entities.entities import Piece
from Entities.constants import ROWS, COLUMNS, RED, YELLOW


class Game:
    def __init__(self, board):
        self.__board = board
        self.__currentPlayer = RED

    def getBoard(self):
        return self.__board.getBoard()

    def checkValidColumn(self, column):
        board = self.__board.getBoard()
        for row in range(ROWS):
            if board[row][column] == 0:
                return True
        return False

    def dropPiece(self, column):
        for row in range(ROWS - 1, -1, -1):
            if self.__board.getBoard()[row][column] == 0:
                self.__board.addPiece(Piece(column, row, self.__currentPlayer))
                self.__currentPlayer = RED if self.__currentPlayer == YELLOW else YELLOW
                break

    def checkVictory(self):
        board = self.__board.getBoard()
        for row in range(ROWS):
            for column in range(COLUMNS - 3):
                try:
                    if board[row][column].color == board[row][column + 1].color and \
                            board[row][column].color == board[row][column + 2].color and \
                            board[row][column].color == board[row][column + 3].color:
                        return True
                except:
                    pass

        for column in range(COLUMNS):
            for row in range(ROWS - 3):
                try:
                    if board[row][column].color == board[row + 1][column].color and \
                            board[row][column].color == board[row + 2][column].color and \
                            board[row][column].color == board[row + 3][column].color:
                        return True
                except:
                    pass

        for row in range(ROWS - 3):
            for column in range(COLUMNS - 3):
                try:
                    if board[row][column].color == board[row + 1][column + 1].color and \
                            board[row][column].color == board[row + 2][column + 2].color and \
                            board[row][column].color == board[row + 3][column + 3].color:
                        return True
                except:
                    pass

        for row in range(3, ROWS):
            for column in range(COLUMNS - 3):
                try:
                    if board[row][column].color == board[row - 1][column + 1].color and \
                            board[row][column].color == board[row - 2][column + 2].color and \
                            board[row][column].color == board[row - 3][column + 3].color:
                        return True
                except:
                    pass

        return False

    def aiMove(self):
        savedBoard = deepcopy(self.__board.getBoard())
        _, bestColumn = self.minimaxAi(4, True)
        self.__board.setBoard(savedBoard)
        self.__currentPlayer = YELLOW
        self.dropPiece(bestColumn)

    def minimaxAi(self, depth, aiTurn):
        if depth == 0 or self.checkVictory():
            if self.checkVictory() and aiTurn is False:
               return depth*10, None
            if self.checkVictory() and aiTurn:
               return depth*(-10), None
            if depth == 0:
                return 0, None
        savedBoard = deepcopy(self.__board.getBoard())
        bestScore = -1000 if aiTurn else 1000
        bestColumn = 0
        for column in range(COLUMNS):
            if self.checkValidColumn(column):
                if aiTurn:
                    self.__board.setBoard(savedBoard)
                    self.__currentPlayer = YELLOW
                    self.dropPiece(column)
                    score, _ = self.minimaxAi(depth - 1, False)
                    if score > bestScore:
                        bestColumn = column
                        bestScore = score
                else:
                    self.__board.setBoard(savedBoard)
                    self.__currentPlayer = RED
                    self.dropPiece(column)
                    score, _ = self.minimaxAi(depth - 1, True)
                    if score < bestScore:
                        bestScore = score
                        bestColumn = column
        return bestScore, bestColumn
