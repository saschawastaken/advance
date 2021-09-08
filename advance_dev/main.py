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
import menu

game_over = True

def game():
    global game_over
    # DISPLAY
    pygame.display.init()
    ws = [500,500]
    display_win = [ws[0] + int(ws[0] * 1/5), ws[1]]
    win = pygame.display.set_mode(display_win)
    pygame.display.set_caption("")
    pygame.display.set_icon(pygame.image.load("img/none.png"))
    # FUNCS
    def bAmmo(player):
        price = 15
        if player.coins > price:
            player.coins -= price
            player.bulletAmmo += 10
    def bBuilding(player):
        price = 20
        if player.coins > price:
            player.coins -= price
            player.build_material += 10
    # OBJECTS
    clock = pygame.time.Clock()
    tps = 60
    g = grid.Grid(50, ws)
    p = player.Player([int(g.rows / 2),g.rows - 2], 'img/test.png')
    enemys = []
    mouseButtonDown = False
    ui = user_interface.UI([ws[0], 0, ws[0] * 1/5, 40])
    ui.add_button("Buy Ammo", bAmmo, (100,100,100), (0,0,0), (0,0,0), (255,255,255))
    ui.add_button("Buy Buildings", bBuilding, (100,100,100), (0,0,0), (0,0,0), (255,255,255))
    # RUNNING
    while not game_over:
        clock.tick(tps)
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
                                p.coins += 10
                            else:
                                    p.coins += len(enemy.path[enemy.path.index(pos):])
                                    for pos2 in enemy.path[enemy.path.index(pos):]:
                                        enemy.path.remove(pos2)
                                    p.bullets.remove(bullet)
                                    break

                            p.score += 1
                        except ValueError:
                            continue
        # ADVANCER SPAWNING
        if randint(0, 100 - p.score) == 0:
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
        # GAME OVER
        for enemy in enemys:
            if enemy.path[-1][1] > g.rows:
                game_over = True
                break
        # GRAPHICS
        win.fill((0,0,0))
        g.show(win, ws)
        p.show(win, g.size, tps)
        for enemy in enemys:
            enemy.show(win, g.size)
        ui.show_items(win, ws, pygame.mouse.get_pos(), mouseButtonDown, ["Score: " + str(p.score), "Coins: " + str(p.coins), "Ammonition: " + str(p.bulletAmmo), "Buildings: " + str(p.build_material), "Buildmode: \"b\""], p)
        mouseButtonDown = False
        pygame.display.update()

while True:
    if game_over:
        menu.run = True
        menu.menu()
        game_over = False
    game()