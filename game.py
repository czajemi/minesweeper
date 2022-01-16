import pygame
import sys
import os
from time import sleep


class Game():
    """Class responsible for the user interface"""

    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        #pieceSize = width, height
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()
        self.__revealMap = False 
        self.__cheatString = "xyzzy"
        self.__currentCheatString = ""

    def run(self):
        """Method responsible for run the game"""
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            #handle pygame events
            for event in pygame.event.get():
                #quit event
                if (event.type == pygame.QUIT):
                    running = False
                #clicking on the mouse event
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
                #entering from the table x, y and z event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x: 
                        self.__currentCheatString += "x"
                    if event.key == pygame.K_y: 
                        self.__currentCheatString += "y"
                    if event.key == pygame.K_z: 
                        self.__currentCheatString += "z"
                    #mines exposure after typing cheatString
                    if self.__currentCheatString == self.__cheatString:
                        self.__revealMap = not self.__revealMap
                        self.__currentCheatString = ""
                    if self.__currentCheatString not in self.__cheatString:
                        self.__currentCheatString = ""
            self.draw()
            pygame.display.flip() #update the screen
            #diplay "Victory!" and play sound if user won, else if user lose display "Game over!" 
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
        #quit the game
        pygame.quit() 
        sys.exit()
    
    def draw(self):
        """Method that draws the board"""
        #start drawing from 0,0 board position
        topLeft = (0 ,0) 
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                #blit - draw one image onto another
                self.screen.blit(image, topLeft)
                #incrementation of topLeft to go throught the board
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1] 

    def loadImages(self):
        """Method responsible for load up the images"""
        #make a new dictionary that maps the name of the image
        self.images = {}
        #listdir returns a list containing the names in folder images
        for fileName in os.listdir("images"):
            #if fileName doesn't ends with .png -> don't add this image to the board
            if(not fileName.endswith(".png")):
                continue
            #grab the image from images folder 
            image = pygame.image.load(r"images/" + fileName)
            #transformation by scaling of the image to piece Size
            image = pygame.transform.scale(image, self.pieceSize)
            #every name before dot has 0 index, set that equals to image object
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        """Method responsible for choose appropriate picture when arter the user action"""
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
        """Method responsible for determining the position of a click by the user"""
        if (self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)

    def message(self, string):
        """Metohod responsible for creating a text and writing it out on the board"""
        font = pygame.font.SysFont("Courier New", 100, bold=pygame.font.Font.bold)
        magenta = (255, 0, 255)
        #render the text and place it on 400,400 position
        text = font.render(string, True, magenta)
        textRect = text.get_rect()
        textRect.center= (400,400)
        self.screen.blit(text, textRect)
        pygame.display.update()