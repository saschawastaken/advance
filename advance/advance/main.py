"""
TODO:
    - Develop bullet direction
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
p = player.Player([int(g.rows / 2),g.rows - 2], 'img/test.png')
a = advancer.Advancer()
# RUNNING
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p.kShoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                p.kShoot = False

    # MOVEMENTS
    p.move(win, pygame.mouse.get_pos(), g.rows)
    a.move(g.rows)
    # INTERACTIONS
    p.shoot()
    # GRAPHICS
    win.fill((0,0,0))
    g.show(win)
    p.show(win, g.rows)
    a.show(win, g.rows)
    pygame.display.update()