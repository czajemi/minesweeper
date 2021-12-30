from game import Game
from board import Board

size = (10, 10)
prob = 0.1
board = Board(size, prob)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()
