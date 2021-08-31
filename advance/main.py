"""
TODO:
    - Player-Bullet Collision Error (Has smth to do with list removing) maybe advancer stacking in one sqaure, need to implement advancer-advancer collision
"""
#
import pygame
from pygame.locals import *
from random import randint
#
import grid
import advancer
import player
import user_interface
# DISPLAY
pygame.display.init()
ws = [500,500]
win = pygame.display.set_mode(ws)
pygame.display.set_caption("ADVANCER")

# OBJECTS
clock = pygame.time.Clock()
fps = 60
ui = user_interface.UI(win)
ui.add_item("Test", (255,0,0), 10)
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
            p.mButtonDown = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                p.BuildMode = not p.BuildMode

    # MOVEMENTS
    p.move(win, pygame.mouse.get_pos(), g.size)
    for enemy in enemys:
        enemy.move(g.rows, p.tiles, enemys)
    # INTERACTIONS
    p.shoot(win, pygame.mouse.get_pos(), g.size)
    ## ENEMY-BULLET COLLISION
    for bullet in p.bullets:
        for enemy in enemys:
            for pos in enemy.path:
                if bullet.rect.colliderect(pygame.Rect(pos[0] * g.size, pos[1] * g.size, g.size, g.size)):
                    try:
                        enemys.remove(enemy)
                        p.bullets.remove(bullet)
                        p.score += 1
                        print("HIT")
                        break
                    except ValueError:
                        continue
    # ADVANCER SPAWNING
    if randint(0, 100) == 0:
        enemys.append(advancer.Advancer(g.rows))
    # GRAPHICS
    win.fill((0,0,0))
    g.show(win)
    ## UI
    ui.show()
    ## SHOWING OBJECTS
    ### PLAYER
    p.show(win, g.size),
    ### ENEMY
    for enemy in enemys:
        enemy.show(win, g.size)
    pygame.display.update()