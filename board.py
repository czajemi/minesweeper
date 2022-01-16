from piece import Piece
from random import random

class Board():
    """Class contains the main game logic"""

    def __init__(self, size, prob):
        #size of the board
        self.size = size
        #probability of the mines placement 
        self.prob = prob 
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.setBoard()

    def setBoard(self):
        """Method responsible for setting the board"""
        #make the list to be a board
        self.board = [[0 for _ in range(self.size[0])] for _ in range(self.size[1])]
        #iterate through the rows and columns of board
        for row in range(self.size[0]):
            for col in range (self.size[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                piece = Piece(hasBomb)
                self.board[row][col] = piece
        self.setNeighbors()
    
    def setNeighbors(self):
        """Method that assigns a list of neighbors to the piece"""
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getListOfNeighbors(self, index):
        """Method which returns the list of neighbors around a piece"""
        neighbors = []
        for row in range(index[0] - 1, index[0]+2):
            for col in range(index[1] -1, index[1]+2):
                #protection against values outside the board
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if(same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors

    def getSize(self):
        """Method responsible for get the size of the board"""
        return self.size

    def getPiece(self, index):
        """Method which gets a piece from index"""
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        """Method responsible for blocking pieces after click and further action in the game"""
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            #it is impossible to click on the piece that has already been clicked or flag
            return False
        #flagging functionality
        if (flag):
            piece.toggledFlag()
            return True
        #left click functionality
        piece.click()
        if (piece.getHasBomb()):
            self.lost = True
            return True
        self.numClicked += 1
        #it is imposible to double click on the piece without any mines around
        if (piece.getNumAround() != 0):
            return True
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getClicked()):
                self.handleClick(neighbor, False)
        return True

    
    def getLost(self):
        """Accessor method which returns lost variable"""
        return self.lost

    def getWon(self):
        """Accessor method which returns true (the user won) if the number of pieces without bombs equals number of clicked pieces"""
        return self.numNonBombs == self.numClicked