import pygame
import sys
from game import Game
from board import Board
from button import Button
from screen import Screen

def ChangeScreen():
    pygame.init()
    colours = {"White": (255, 255, 255), "Lime": (0, 255, 0), "Magenta": (255, 0, 255)}
    menuScreen = Screen("Menu Screen")
    gameScreen = Screen("Miniesweeper")
    pygame.font.init()
    menuScreen.makeCurrent()
    startButton = Button(300, 400, 150, 50, colours["Lime"], colours["Magenta"], "arial", 20, colours["White"], "Start")

    while True:
        menuScreen.screenUpdate()
        gameScreen.screenUpdate()
        mousePosition = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        
        if menuScreen.checkUpdate():
            button = startButton.focusCheck(mousePosition, mouseClick)
            startButton.showButton(menuScreen.returnTitle())
            if button:
                gameScreen.makeCurrent()
                menuScreen.endCurrent()
        elif gameScreen.checkUpdate():
            size = (10, 10)
            prob = 0.1
            board = Board(size, prob)
            screenSize = (800, 800)
            game = Game(board, screenSize)
            second = game.run()

            if second:
                menuScreen.makeCurrent()
                gameScreen.endCurrent()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()