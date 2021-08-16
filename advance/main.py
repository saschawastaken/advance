"""
TODO:
    - Bullet shooting velocity fixing
    - Building function
    - Bullet ammonition and ammonition-interface top-left
"""
#
import pygame
from pygame.locals import *
from random import randint
#
import grid
import advancer
import player
# DISPLAY
pygame.display.init()
ws = [500,500]
win = pygame.display.set_mode(ws)
pygame.display.set_caption("ADVANCER")
# FONT
pygame.font.init()
globalFontSize = 15
globalFont = pygame.font.SysFont('calibri', globalFontSize)
text = globalFont.render('kek', False, (255,0,0))
# OBJECTS
clock = pygame.time.Clock()
fps = 60
g = grid.Grid(50, win)
p = player.Player([int(g.rows / 2),g.rows - 2], 'img/test.png')
enemys = []
# RUNNING
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            p.kShoot = True

    # MOVEMENTS
    p.move(pygame.mouse.get_pos(), g.size)
    for enemy in enemys:
        enemy.move(g.rows)
    # INTERACTIONS
    p.shoot(win, pygame.mouse.get_pos(), g.size)
    ## ENEMY-BULLET COLLISION
    try:
        for bullet in p.bullets:
            for enemy in enemys:
                for pos in enemy.path:
                    if bullet.rect.colliderect(pygame.Rect(pos[0] * g.size, pos[1] * g.size, g.size, g.size)):
                        enemys.remove(enemy)
                        break
    except IndexError: pass  
    # ADVANCER SPAWNING
    if randint(0, 100) == 0:
        enemys.append(advancer.Advancer())
    # GRAPHICS
    win.fill((0,0,0))
    win.blit(text, (25,25))
    g.show(win)
    p.show(win, g.size)
    for enemy in enemys:
        enemy.show(win, g.size)
    
    pygame.display.update()