#
import pygame
import math
#
from bullet import Bullet
from tile import Tile
class Player():

    def __init__(self, pos, imgURL) -> None:
        # *Key elements marked with k at beginning
        self.pos = pos
        self.imgAngle = 0
        # GRAPHICAL
        self.img = pygame.image.load(imgURL)
        self.color = (0,255,0)
        # INTERACTIONS (Key elements marked with k at beginning)
        self.score = 0
        self.bullets = []
        self.bulletAmmo = 30
        self.mButtonDown = False
        # BUILD ACTION
        self.tiles = []
        self.build_material = 30
        self.BuildMode = False
        
    def show(self, win, size):
        img_copy = pygame.transform.rotate(self.img, self.imgAngle)
        win.blit(img_copy, (self.pos[0] * size - int(img_copy.get_width() / 2) , self.pos[1] * size - int(img_copy.get_height() / 2 )))
        for bullet in self.bullets:
            bullet.show(win, size)
        for t in self.tiles:
            t.show(win, size)

    def move(self, win, mousePos, size):
        # PLAYER ROTATING
        mx, my = mousePos

        opposite_leg = mx - self.pos[0] * size
        adjacent_leg = self.pos[1] * size - my

        if adjacent_leg > 0: self.imgAngle = 90 - math.degrees(math.atan(opposite_leg / adjacent_leg))

        for bullet in self.bullets:
            bullet.move()

        if self.BuildMode:
            self.build(win, size, mousePos)

    def shoot(self, win, mousePos, size):
        if self.mButtonDown and not self.BuildMode:
            if self.bulletAmmo > 0:
                pos_x, pos_y = self.pos
                mx, my = mousePos

                opposite_leg = mx - self.pos[0] * size
                adjacent_leg = self.pos[1] * size - my

                if adjacent_leg > 0: self.bullets.append(Bullet([pos_x, pos_y], (opposite_leg / adjacent_leg) * -1, 1, self.imgAngle + 90))

                self.mButtonDown = False
                self.bulletAmmo -= 1
        # REMOVING BULLETS WHEN THEY GET OUTSIDE THE WINDOW
        for b in self.bullets:
            if b.pos[0] * size < 0 or b.pos[0] * size > win.get_width() or b.pos[1] * size < 0:
                self.bullets.remove(b)

    def build(self, win, size, mousePos):
        if self.mButtonDown:
            rows = win.get_width() / size

            pos = [math.floor(mousePos[0] / win.get_width() * rows), 
                   math.floor(mousePos[1] / win.get_height() * rows)]

            identicTiles = False
            for t in self.tiles:
                if pos == t.pos:
                    identicTiles = not identicTiles

            if not identicTiles:
                self.tiles.append(Tile(pos))
                
            self.mButtonDown = False
