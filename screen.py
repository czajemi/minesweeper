import pygame

class Screen():
    def __init__(self, title, width=800, height=800, fill=(255,255,255)):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False

    def makeCurrent(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode((self.width, self.height))

    def endCurrent(self):
        self.current = False

    def checkUpdate(self):
        return self.current

    def screenUpdate(self):
        if(self.current):
            self.screen.fill(self.fill)

    def returnTitle(self):
        return self.screen
