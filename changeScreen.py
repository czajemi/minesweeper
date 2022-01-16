import pygame
import sys
from game import Game
from board import Board
from button import Button
from screen import Screen

def ChangeScreen():
    """Function for changing screen after clicking Start Button and displays predefined graphics on current screen"""
    # initialize pygame module
    pygame.init()
    colours = {"White": (255, 255, 255), "Lime": (0, 255, 0), "Magenta": (255, 0, 255)}
    #definition of two screens
    menuScreen = Screen("Menu Screen")
    gameScreen = Screen("Miniesweeper")
    #initialize the font module
    pygame.font.init()
    #at the begining the current screen is menu Screen
    menuScreen.makeCurrent()
    #definition of a start button
    startButton = Button(300, 400, 150, 50, colours["Lime"], colours["Magenta"], "Courier New", 30, colours["White"], "Start")
    while True:
        menuScreen.screenUpdate()
        gameScreen.screenUpdate()
        mousePosition = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        #checking which screen is current
        if menuScreen.checkUpdate():
            #checking mouse position and displaying of the start button
            button = startButton.focusCheck(mousePosition, mouseClick)
            startButton.showButton(menuScreen.returnTitle())
            if button:
                #after clicking a start button the current screen is changing
                gameScreen.makeCurrent()
                menuScreen.endCurrent()
        elif gameScreen.checkUpdate():
            #display the second sreen with the game board
            size = (10, 10)
            prob = 0.1
            board = Board(size, prob)
            screenSize = (800, 800)
            game = Game(board, screenSize)
            second = game.run()

            if second:
                menuScreen.makeCurrent()
                gameScreen.endCurrent()
        
        #quit the game event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()