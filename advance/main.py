"""
TODO:
    - Menu
"""
#
import pygame
from pygame.locals import *
from random import randint

from pygame.sprite import collide_mask
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
# FUNCS
def bAmmo(player):
    if player.score > 0:
        player.score -= 15
        player.bulletAmmo += 10
def bBuilding(player):
    if player.score > 0:
        player.score -= 20
        player.build_material += 10
# OBJECTS
clock = pygame.time.Clock()
fps = 120
g = grid.Grid(50, ws)
p = player.Player([int(g.rows / 2),g.rows - 2], 'img/test.png')
enemys = []
mouseButtonDown = False
ui = user_interface.UI([ws[0], 0, ws[0] * 1/5, 40])
ui.add_button("Buy Ammo", bAmmo, (100,100,100), (0,0,0))
ui.add_button("Buy Buildings", bBuilding, (100,100,100), (0,0,0))
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
        ran_pos_x = randint(0, g.rows - 1)
        collision_check = True
        for enemy in enemys:
            if ran_pos_x == enemy.path[0][0]:
                collision_check = False
        if collision_check:
            enemys.append(advancer.Advancer(ran_pos_x))
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
    ui.show_items(win, ws, pygame.mouse.get_pos(), mouseButtonDown, ["Score: " + str(p.score), "Ammonition: " + str(p.bulletAmmo), "Buildings: " + str(p.build_material)], p)
    mouseButtonDown = False
    pygame.display.update()


    if __name__ == "__main__":
        print("TRUE")