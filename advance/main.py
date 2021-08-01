"""
TODO:
    - Learn about Trigonometry
    - Implement Image turning for pplayer based on mouse position using trigonometry
    - Develop bullet-object
"""

#
from player import Player
import pygame
from pygame.locals import *
import math
#
import grid
import advancer
import player
# DISPLAY
pygame.display.init()
ws = [500,500]
win = pygame.display.set_mode(ws)
pygame.display.set_caption("ADVANCER")

# OBJECTS
clock = pygame.time.Clock()
fps = 60
g = grid.Grid(50)
p = player.Player([25,47], 'img/test.png')
# RUNNING
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass
    # MOVEMENTS
    # GRAPHICS
    win.fill((0,0,0))
    # {
    g.show(win)
    p.show(win, g.rows)
    pygame.draw.line(win, (255,0,0), (50, win.get_height()), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    pygame.draw.line(win, (255,0,0), (pygame.mouse.get_pos()[0], win.get_height()), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    width = pygame.mouse.get_pos()[0] - 50
    height = pygame.mouse.get_pos()[1] - win.get_height()
    hy_length = math.sqrt(math.pow(width, 2) + math.pow(height, 2))
    ka_length = win.get_height() - pygame.mouse.get_pos()[1]
    # } 
    pygame.display.update()