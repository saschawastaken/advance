#
import pygame
import math

from pygame import mouse
#
import bullet

class Player():

    def __init__(self, pos, imgURL) -> None:
        # *Key elements marked with k at beginning
        self.pos = pos
        self.imgAngle = 0
        # GRAPHICAL
        self.img = pygame.image.load(imgURL)
        self.color = (0,255,0)
        # INTERACTIONS (Key elements marked with k at beginning)
        self.bullets = []
        self.kShoot = False
        # BUILD ACTION
        self.kBuildMode = False
        
    def show(self, win, rows):
        size = win.get_width() / rows
        img_copy = pygame.transform.rotate(self.img, self.imgAngle)
        win.blit(img_copy, (self.pos[0] * size - int(img_copy.get_width() / 2) , self.pos[1] * size - int(img_copy.get_height() / 2 )))
        for bullet in self.bullets:
            bullet.show(win, rows)

    def move(self, win, mousePos, rows):
        # PLAYER ROTATING
        mx, my = mousePos
        size = win.get_width() / rows

        opposite_leg = mx - self.pos[0] * size
        adjacent_leg = self.pos[1] * size - my

        if adjacent_leg > 0: self.imgAngle = 90 - math.degrees(math.atan(opposite_leg / adjacent_leg))

        for bullet in self.bullets:
            bullet.move(win, mousePos, rows)

    def shoot(self, win, mousePos, rows):
        if self.kShoot:
            pos_x, pos_y = self.pos
            mx, my = mousePos
            size = win.get_width() / rows

            opposite_leg = mx - self.pos[0] * size
            adjacent_leg = self.pos[1] * size - my

            if adjacent_leg > 0: self.bullets.append(bullet.Bullet([pos_x, pos_y], (opposite_leg / adjacent_leg) * -1, 1, self.imgAngle + 90))

            self.kShoot = False

    def build(self):
        pass