import pygame

class Button():
    def __init__(self, x, y, sx, sy, bcolour, fbcolour, font, fontSize, fcolour, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.bcolour = bcolour
        self.fbcolour = fbcolour
        self.font = font
        self.fontSize = fontSize
        self.fcolour = fcolour
        self.text = text
        self.current = False
        self.xCor = lambda x, sx, fontSize, text: x + (sx/2) - (fontSize/2)*(len(text)/2) - 5
        self.yCor = lambda y, sy, fontSize: y + (sy/2) - (fontSize/2) - 4
        self.add = lambda x, y: x + y
        self.buttonf = pygame.font.SysFont(font, fontSize)

    def showButton(self, display):
        if(self.current):
            pygame.draw.rect(display, self.fbcolour, (self.x, self.y, self.sx, self.sy))
        else:
            pygame.draw.rect(display, self.bcolour, (self.x, self.y, self.sx, self.sy))
        textSurface = self.buttonf.render(self.text, False, self.fcolour)
        
        display.blit(textSurface,((self.xCor(self.x, self.sx, self.fontSize, self.text), self.yCor(self.y, self.sy, self.fontSize))))

    def focusCheck(self, mousePos, mouseClick):
        if(mousePos[0] >= self.x and mousePos[0] <= self.add(self.x, self.sx) and mousePos[1] >= self.y and mousePos[1] <= self.add(self.y, self.sy)):
            self.current = True
            return mouseClick[0]
        else:
            self.current = False
            return False