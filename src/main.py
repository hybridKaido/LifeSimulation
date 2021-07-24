import pygame
from classes import *

fps = 60
res = (600, 300)
display = pygame.display.set_mode(res)
run = True
Cells = []

while run:
    clock = pygame.time.Clock()
    clock.tick(fps)
    display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cell = spawnCell(res, 5, (pygame.mouse.get_pos()))
            Cells.append(cell)
    
    for cell in Cells:
        cell.draw(display)
        cell.move(fps)
    pygame.display.flip()

pygame.quit()