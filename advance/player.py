#
import pygame
import math
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
        self.bulletAmmo = 30
        self.kShoot = False
        # BUILD ACTION
        self.kBuildMode = False
        
    def show(self, win, size):
        img_copy = pygame.transform.rotate(self.img, self.imgAngle)
        win.blit(img_copy, (self.pos[0] * size - int(img_copy.get_width() / 2) , self.pos[1] * size - int(img_copy.get_height() / 2 )))
        for bullet in self.bullets:
            bullet.show(win, size)

    def move(self, mousePos, size):
        # PLAYER ROTATING
        mx, my = mousePos

        opposite_leg = mx - self.pos[0] * size
        adjacent_leg = self.pos[1] * size - my

        if adjacent_leg > 0: self.imgAngle = 90 - math.degrees(math.atan(opposite_leg / adjacent_leg))

        for bullet in self.bullets:
            bullet.move()

    def shoot(self, win, mousePos, size):
        if self.kShoot:
            if self.bulletAmmo > 0:
                pos_x, pos_y = self.pos
                mx, my = mousePos

                opposite_leg = mx - self.pos[0] * size
                adjacent_leg = self.pos[1] * size - my

                if adjacent_leg > 0: self.bullets.append(bullet.Bullet([pos_x, pos_y], (opposite_leg / adjacent_leg) * -1, 1, self.imgAngle + 90))

                self.kShoot = False
                self.bulletAmmo -= 1
        # REMOVING BULLETS WHEN THEY GET OUTSIDE THE WINDOW
        for b in self.bullets:
            if b.pos[0] * size < 0 or b.pos[0] * size > win.get_width() or b.pos[1] * size < 0:
                self.bullets.remove(b)

    def build(self):
        pass