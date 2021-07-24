import pygame
from random import *

def spawnCell(res, size, pos):
    cell = Cell(res, size)
    cell.posx = pos[0]
    cell.posy = pos[1]
    return cell

class Cell():
    
    def __init__(self, ground, size):
        self.color = (randrange(255), randrange(255), randrange(255))
        self.posx = randrange(0, ground[0])
        self.posy = randrange(0, ground[1])
        self.size = size
        self.mx = 0
        self.my = 0
        self.ttm = randrange(2, 5)
        self.ground = ground

    def changeDir(self):
        self.mx = randrange(-1, 2)
        self.my = randrange(-1, 2)

    def move(self):
        self.posx += self.mx
        self.posy += self.my
        
        self.changeDir() 

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.posx, self.posy), self.size, width=0)
