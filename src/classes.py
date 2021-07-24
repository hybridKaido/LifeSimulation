import pygame
from random import *
import math


def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

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
        self.health = randrange(70, 120)
        self.attackPower = randrange(10, 25)
        self.isDead = False

    def changeDir(self):
        self.mx = randrange(-1, 2)
        self.my = randrange(-1, 2)

    def move(self, fps):
        self.tick += 1
        if self.posx + self.mx >= self.ground[0] or self.posx + self.mx <= 0:
            self.mx = -self.mx
        if self.posy + self.my >= self.ground[1] or self.posy + self.my <= 0:
            self.my  = -self.my
        else:
            self.posx += self.mx
            self.posy += self.my

        if(self.tick > fps * self.ttm):
            self.changeDir()
            self.tick = 0

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.posx, self.posy), self.size, width=0)

    def eat(self, target):
        target.health -= self.attackPower
        
    def die(self, Cells):
        if(self.health < 0):
            Cells.remove(self)

    def run(self):
        pass

    def logic(self, Cells):
        for cell in Cells:
            if((calculateDistance(self.posx, self.posy, cell.posx, cell.posy) < 10) and len(Cells) > 1 and cell != self):
                cell.eat(cell)
                cell.die(Cells)