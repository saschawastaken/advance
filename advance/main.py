"""
TODO:
    - Score calculation
    - Right Player movement
    - Menu
    - Button class & implement them at right
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
display_win = [ws[0] + int(ws[0] * 1/5), ws[1]]
win = pygame.display.set_mode(display_win)
pygame.display.set_caption("ADVANCER")
# OBJECTS
clock = pygame.time.Clock()
fps = 120
ui = user_interface.UI([ws[0], 0, ws[0] * 1/5, 40])
ui.add_button("Buy Ammo", (100,100,100), (0,0,0))
ui.add_button("Buy Buildings", (100,100,100), (0,0,0))
g = grid.Grid(50, ws)
p = player.Player([int(g.rows / 2),g.rows - 2], 'img/test.png')
enemys = []
mouseButtonDown = False
# RUNNING
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            p.mButtonDown = True
            mouseButtonDown = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                p.BuildMode = not p.BuildMode
    # MOVEMENTS & Implemented Interactions
    p.move(win, ws, pygame.mouse.get_pos(), mouseButtonDown, g.size)
    for enemy in enemys:
        enemy.move(p.tiles, enemys, g.rows)
    ## ENEMY-BULLET COLLISION
    for bullet in p.bullets:
        for enemy in enemys:
            for pos in enemy.path:
                if bullet.rect.colliderect(pygame.Rect(pos[0] * g.size, pos[1] * g.size, g.size, g.size)):
                    try:
                        if pos == enemy.path[-1]:
                            enemys.remove(enemy)
                            p.bullets.remove(bullet)
                            p.score += 10
                        else:
                                p.score += len(enemy.path[enemy.path.index(pos):])
                                for pos2 in enemy.path[enemy.path.index(pos):]:
                                    enemy.path.remove(pos2)
                                p.bullets.remove(bullet)
                                break
                    except ValueError:
                        continue
    # ADVANCER SPAWNING
    if randint(0, 100) == 0:
        enemys.append(advancer.Advancer(g.rows))
    # ADVANCER REMOVING
    for enemy in enemys:
        if len(enemy.path) < 1:
            enemys.remove(enemy)
    # GRAPHICS
    win.fill((0,0,0))
    g.show(win, ws)
    p.show(win, g.size)
    for enemy in enemys:
        enemy.show(win, g.size)
    ui.show_items(win, ws, ["Score: " + str(p.score), "Ammonition: " + str(p.bulletAmmo), "Buildings: " + str(p.build_material)])
    ui.show_buttons(win, pygame.mouse.get_pos(), mouseButtonDown)
    mouseButtonDown = False
    pygame.display.update()