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
        self.ttm = 1
        self.ground = ground
        self.tick = 0

    def changeDir(self):
        self.mx = randrange(-1, 2)
        self.my = randrange(-1, 2)

    def move(self, fps):
        self.tick += 1
        self.posx += self.mx
        self.posy += self.my

        if(self.tick > fps * self.ttm):
            self.changeDir()
            self.tick = 0

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.posx, self.posy), self.size, width=0)
