"""
TODO:
    - Bullet shooting velocity fixing
    - Building function
"""
#
import pygame
from pygame.locals import *
from random import randint
#
import grid
import advancer
import player
import tile
# DISPLAY
pygame.display.init()
ws = [500,500]
win = pygame.display.set_mode(ws)
pygame.display.set_caption("ADVANCER")
# FONT
pygame.font.init()
def getText(text, size, fontStyle, color, isBald=False):
    font = pygame.font.SysFont(fontStyle, size)
    rendered = font.render(text, isBald, color)
    return rendered

# OBJECTS
clock = pygame.time.Clock()
fps = 60
g = grid.Grid(50, win)
p = player.Player([int(g.rows / 2),g.rows - 2], 'img/test.png')
enemys = []
t = tile.Tile([0, 0], [3, 0])
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
                        p.bullets.remove(bullet)
                        p.score += 1
                        break
    except IndexError: pass  
    # ADVANCER SPAWNING
    if randint(0, 100) == 0:
        enemys.append(advancer.Advancer())
    # GRAPHICS
    win.fill((0,0,0))
    g.show(win)
    # SHOWING SCORE
    textScore = getText("Score: " + str(p.score), 15, 'calibri', (255,255,255), True)
    win.blit(textScore, (win.get_width() - textScore.get_width(), 0))
    # SHOWING AMMONITION 
    textAmmo = getText("Ammo: " + str(p.bulletAmmo), 15, 'calibri', (255,255,255), True)
    win.blit(textAmmo, (win.get_width() - textAmmo.get_width(), textScore.get_height()))
    # SHOWING OBJECTS
    p.show(win, g.size)
    t.show(win, g.size)
    for enemy in enemys:
        enemy.show(win, g.size)
    
    pygame.display.update()