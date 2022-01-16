import pygame

class Screen():
    """Class responsible for screen definition"""

    def __init__(self, title, width=800, height=800, fill=(255,255,255)):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False

    def makeCurrent(self):
        """Method responsible for making screen current, displaying the window title and initialisation of the screen"""
        #display the current window title like Menu Screen or Miniesweeper
        pygame.display.set_caption(self.title)
        self.current = True
        #initialize the screen for display
        self.screen = pygame.display.set_mode((self.width, self.height))

    def endCurrent(self):
        """Method that changes screen from current to not current"""
        self.current = False

    def checkUpdate(self):
        """Method that is used for checking if the screen has been set as current"""
        return self.current

    def screenUpdate(self):
        """Method responsible for updating the screen"""
        if(self.current):
            self.screen.fill(self.fill)

    def returnTitle(self):
        """Accessor method that returns title of the screen"""
        return self.screen
