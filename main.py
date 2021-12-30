from game import Game
from board import Board

size = (15, 15)
prob = 0.5
board = Board(size, prob)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()
