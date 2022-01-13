import unittest
from board import Board

class TestGame(unittest.TestCase):
    """Class responsible for testing the game"""

    def test_numberOfMinesAround(self):
        """After clicking, the number of mines adjacent to the field is displayed"""
        board = Board((10,10), 0)
        self.assertTrue(board.getPiece((2,2)).getNumAround()== 0)
        board = Board((10,10), 1)
        self.assertTrue(board.getPiece((2,2)).getNumAround()== 8)
    
    def test_displayMine(self):
        """Clicking on the field, the mine is displayed, the game is over"""
        board = Board((10,10), 1)
        piece = board.getPiece((2,2))
        board.handleClick(piece, False)
        self.assertTrue(board.getLost())
    
    def test_noMinesInNeighborhood(self):
        """Clicking on the field, no mines in the neighborhood"""
        board = Board((10,10), 0)
        board.handleClick(board.getPiece((2,2)), False)
        anyFieldLeft = False
        for row in board.board:
            for piece in row:
                if not piece.getClicked():
                    anyFieldLeft = True
        self.assertFalse(anyFieldLeft)

    def test_clickigPiecesWithoutMines(self):
        """Win the game by clicking all pieces without mines"""
        board = Board((10,10), 0)
        board.handleClick(board.getPiece((2,2)), False)
        self.assertTrue(board.getWon())
        
    def test_flaggingPiecesWithMines(self):
        """Win the game by flagging all mine pieces"""
        board = Board((10,10), 1)
        for row in board.board:
            for piece in row:
                board.handleClick(piece, True)
        self.assertTrue(board.getWon())
        
    def test_flagCheckedField(self):
        """Attempting to flag a checked field - expected failure"""
        board = Board((10,10), 0)
        piece = board.getPiece((2,2))
        self.assertTrue(board.handleClick(piece, False))
        self.assertFalse(board.handleClick(piece, True))

if __name__ == '__main__':
    unittest.main()