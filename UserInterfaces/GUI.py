from time import sleep

import pygame

from Entities.constants import RED, BLUE, ROWS, WINDOW_HEIGHT, WINDOW_WIDTH, SQUARE_SIZE, COLUMNS, BLACK, PIECE_RADIUS, \
    PADDING, YELLOW, WHITE
from Entities.exceptions import FullColumnError


class GUI:
    def __init__(self, game):
        self.__game = game
        pygame.init()
        self.__screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Connect4')
        self.__runningProgram()

    def __runningProgram(self):
        FPS = 60
        gameOver = False
        currentPlayer = RED
        fpsCounter = pygame.time.Clock()
        while not gameOver:
            self.__drawBoard()
            pygame.display.update()
            fpsCounter.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if currentPlayer == RED:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        inputColumn = self.__getColumnMouse(pygame.mouse.get_pos())
                        if not self.__game.checkValidColumn(inputColumn):
                            raise FullColumnError("The column is full")
                        self.__game.dropPiece(inputColumn)
                        if self.__game.checkVictory():
                            self.__drawBoard()
                            self.__displayWinner("RED")
                            pygame.display.update()
                            sleep(5)
                            gameOver = True
                        currentPlayer = YELLOW

            self.__drawBoard()
            pygame.display.update()

            if currentPlayer == YELLOW and not gameOver:
                self.__game.aiMove()
                if self.__game.checkVictory():
                    self.__drawBoard()
                    self.__displayWinner("YELLOW")
                    pygame.display.update()
                    sleep(5)
                    gameOver = True
                currentPlayer = RED

    def __drawBoard(self):
        self.__screen.fill(BLUE)
        board = self.__game.getBoard()
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == 0:
                    pygame.draw.circle(self.__screen, BLACK,
                                       (column * SQUARE_SIZE + PIECE_RADIUS, row * SQUARE_SIZE + PIECE_RADIUS),
                                       PIECE_RADIUS - PADDING)
                else:
                    pygame.draw.circle(self.__screen, board[row][column].color,
                                       (column * SQUARE_SIZE + PIECE_RADIUS, row * SQUARE_SIZE + PIECE_RADIUS),
                                       PIECE_RADIUS - PADDING)

    def __getColumnMouse(self, position):
        xPosition, _ = position
        return xPosition // SQUARE_SIZE

    def __displayWinner(self, winner):
        comicSans = pygame.font.Font('ComicSansMS3.ttf', 64)
        winnerText = comicSans.render(f"{winner} WON!", True, WHITE)
        winnerTextBox = winnerText.get_rect()
        winnerTextBox.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.__screen.blit(winnerText, winnerTextBox)
