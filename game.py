import pygame 
import os
from time import sleep

from board import Board

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption("Minesweeper")
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if(self.board.getWon()):
                #information about win
                font = pygame.font.SysFont("Courier New", 100, bold=pygame.font.Font.bold)
                magenta = (255, 0, 255)
                text = font.render('Victory!', True, magenta)
                textRect = text.get_rect()
                textRect.center= (400,400)
                self.screen.blit(text, textRect)
                pygame.display.update()
                sleep(7)
                running = False

        pygame.quit()
    
    def draw(self):
        topLeft = (0 ,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1] 

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if(not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        string = None
        if(piece.getClicked()):
            string = "bomb" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flagged" if piece.getFlagged() else "block"
        return self.images[string]

    def handleClick(self, position, rightClick):
        if (self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)

    
