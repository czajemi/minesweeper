class Piece():
    """Class responsible for representation of an individual piece"""

    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

    def getHasBomb(self):
        """Accessor method which returns information about bomb on the piece"""
        return self.hasBomb

    def getClicked(self):
        """Accessor method which returns whether a piece is clicked"""
        return self.clicked

    def getFlagged(self):
        """Accessor method which returns whether a piece is flagged"""
        return self.flagged
    
    def setNeighbors(self, neighbors):
        """Method responsible for setting the neighbors of a piece"""
        self.neighbors = neighbors
        self.setNumAround()
    
    def setNumAround(self):
        """Method which counts the number of mines around the piece"""
        self.numAround = 0
        for piece in self.neighbors:
            if(piece.getHasBomb()):
                self.numAround += 1

    def getNumAround(self):
        """Accessor method which returns number of mines around the piece"""
        return self.numAround

    def toggledFlag(self):
        """Method wherein the flagged piece was changed to an unflagged piece"""
        self.flagged = not self.flagged

    def click(self):
        """Method that returns that the piece is clicked"""
        self.clicked = True

    def getNeighbors(self):
        """Accessor method which returns list of the piece neighbors"""
        return self.neighbors