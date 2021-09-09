import pygame
import math
from bullet import Bullet
from tile import Tile

class Player():

    def __init__(self, pos, imgURL) -> None:
        self.pos = pos
        self.imgAngle = 0
        self.img = pygame.image.load(imgURL)
        self.color = (0,255,0)
        self.coins = 0
        self.score = 0
        self.bullets = []
        self.bulletAmmo = 5
        self.mButtonDown = False
        self.tiles = []
        self.t_live_counter = 0
        self.build_material = 0
        self.BuildMode = False
        
    def show(self, win, size, tps):
        img_copy = pygame.transform.rotate(self.img, self.imgAngle)
        win.blit(img_copy, (self.pos[0] * size - int(img_copy.get_width() / 2) , self.pos[1] * size - int(img_copy.get_height() / 2 )))
        
        for bullet in self.bullets:
            bullet.show(win, size)

        for t in self.tiles:
            t.show(win, size)
            if t.lifetime > 1:
                if t.tick_live_counter >= tps:
                    t.lifetime -= 1
                    t.tick_live_counter = 0
            else:
                self.tiles.remove(t)

            t.tick_live_counter += 1

    def move(self, ws, mousePos, mButtonDown, size):
        mx, my = mousePos

        opposite_leg = mx - self.pos[0] * size
        adjacent_leg = self.pos[1] * size - my

        if adjacent_leg > 0: self.imgAngle = 90 - math.degrees(math.atan(opposite_leg / adjacent_leg))

        for bullet in self.bullets:
            bullet.move()

        if self.BuildMode:
            self.build(ws, size, mousePos, mButtonDown)
        else:
            self.shoot(ws, mousePos, mButtonDown, size)

    def shoot(self, ws, mousePos, mButtonDown, size):
        if mButtonDown and not self.BuildMode and mousePos[0] < ws[0]:
            if self.bulletAmmo > 0:
                pos_x, pos_y = self.pos
                mx, my = mousePos

                opposite_leg = mx - self.pos[0] * size
                adjacent_leg = self.pos[1] * size - my

                if adjacent_leg > 0:
                    self.bullets.append(Bullet([pos_x, pos_y], (opposite_leg / adjacent_leg) * -1, 1, self.imgAngle + 90))

                self.bulletAmmo -= 1

        for b in self.bullets:
            if b.pos[0] * size < 0 or b.pos[0] * size > ws[0] or b.pos[1] * size < 0:
                self.bullets.remove(b)

    def build(self, ws, size, mousePos, mButtonDown):
        if self.build_material > 0 and mousePos[0] < ws[0]:
            if mButtonDown:
                rows = ws[0] / size

                pos = [math.floor(mousePos[0] / ws[0] * rows), 
                    math.floor(mousePos[1] / ws[1] * rows)]

                identicTiles = False
                for t in self.tiles:
                    if pos == t.pos:
                        identicTiles = not identicTiles

                if not identicTiles:
                    self.tiles.append(Tile(pos))
                    self.build_material -= 1
