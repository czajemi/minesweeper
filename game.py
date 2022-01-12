import pygame
import sys
import os
from time import sleep


class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()
        self.__revealMap = False 
        self.__cheatString = "xyzzy"
        self.__currentCheatString = ""

    def run(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x: 
                        self.__currentCheatString += "x"
                    if event.key == pygame.K_y: 
                        self.__currentCheatString += "y"
                    if event.key == pygame.K_z: 
                        self.__currentCheatString += "z"
                    if self.__currentCheatString == self.__cheatString:
                        self.__revealMap = not self.__revealMap
                        self.__currentCheatString = ""
                    if self.__currentCheatString not in self.__cheatString:
                        self.__currentCheatString = ""
            self.draw()
            pygame.display.flip()
            if(self.board.getWon()):
                text = "Victory!"
                sound = pygame.mixer.Sound("winSound.wav")
                sound.play()
                self.message(text)
                sleep(3)
                running = False
            elif(self.board.getLost()):
                text = "Game over!"
                self.message(text)
                sleep(2)
                running = False
        pygame.quit()
        sys.exit()
    
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
            if self.__revealMap and piece.getHasBomb():
                string = "bomb_unclicked"
            elif piece.getFlagged():
                string = "flagged"
            else:
                string = "block"
        return self.images[string]

    def handleClick(self, position, rightClick):
        if (self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)

    def message(self, string):
        font = pygame.font.SysFont("Courier New", 100, bold=pygame.font.Font.bold)
        magenta = (255, 0, 255)
        text = font.render(string, True, magenta)
        textRect = text.get_rect()
        textRect.center= (400,400)
        self.screen.blit(text, textRect)
        pygame.display.update()