import pygame

class Button():
    """Class responsible for start button operation"""

    def __init__(self, x, y, sx, sy, bcolour, fbcolour, font, fontSize, fcolour, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        #colour of the button when the mouse cursor isn't on it
        self.bcolour = bcolour
        #colour of the button when the mouse cursor is on it
        self.fbcolour = fbcolour
        self.font = font
        self.fontSize = fontSize
        #font colour
        self.fcolour = fcolour
        self.text = text
        self.current = False
        self.xCor = lambda x, sx, fontSize, text: x + (sx/2) - (fontSize/2)*(len(text)/2) - 5
        self.yCor = lambda y, sy, fontSize: y + (sy/2) - (fontSize/2) - 4
        self.add = lambda x, y: x + y
        self.buttonf = pygame.font.SysFont(font, fontSize)

    def showButton(self, display):
        """Method responsible for displaying the start button on the screen"""
        #button display depends on whether the mouse cursor is on the button or not
        #it was written with if statement
        if(self.current):
            pygame.draw.rect(display, self.fbcolour, (self.x, self.y, self.sx, self.sy))
        else:
            pygame.draw.rect(display, self.bcolour, (self.x, self.y, self.sx, self.sy))
        #surface for the text
        textSurface = self.buttonf.render(self.text, False, self.fcolour)
        #display the button
        display.blit(textSurface,((self.xCor(self.x, self.sx, self.fontSize, self.text), self.yCor(self.y, self.sy, self.fontSize))))

    def focusCheck(self, mousePos, mouseClick):
        """Method responsible for checking focus, which depends on mouse position"""
        #check the position of the mouse and if it is on the button then current is True
        if(mousePos[0] >= self.x and mousePos[0] <= self.add(self.x, self.sx) and mousePos[1] >= self.y and mousePos[1] <= self.add(self.y, self.sy)):
            self.current = True
            return mouseClick[0]
        else:
            self.current = False
            return False