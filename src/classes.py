import pygame
from random import *
import math


def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def spawnCell(res, pos):
    cell = Cell(res)
    cell.posx = pos[0]
    cell.posy = pos[1]
    return cell

class Cell():
    
    def __init__(self, ground):
        self.color = (randrange(255), randrange(255), randrange(255))
        self.posx = randrange(0, ground[0])
        self.posy = randrange(0, ground[1])
        self.size = randrange(4, 10)
        self.mx = 0
        self.my = 0
        self.ttm = 1
        self.ground = ground
        self.tick = 0
        self.health = randrange(70, 120)
        self.attackPower = randrange(30, 40)
        self.isDead = False
        self.attackRange = randrange(10, 30)
        self.recharge = randrange(1, 3)
        self.attackTick = 0

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

    def logic(self, Cells, fps):
        
        for cell in Cells:
            if((calculateDistance(self.posx, self.posy, cell.posx, cell.posy) < self.attackRange) and len(Cells) > 1 and cell != self and self.attackTick > self.recharge * fps):
                cell.eat(cell)
                cell.die(Cells)
        if self.attackTick > fps * self.recharge:
            self.attackTick = 0