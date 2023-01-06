from Repository.Repository import Board
from Service.Service import Game
from UserInterfaces.GUI import GUI
from UserInterfaces.UI import UI

if __name__ == "__main__":
    board = Board()
    game = Game(board)
    ui = GUI(game)
