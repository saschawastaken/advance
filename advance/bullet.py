import pygame
import math

class Bullet():

    def __init__(self, pos, vel_x, vel_y, imgAngle) -> None:
        # GRAPHICS
        self.img = pygame.image.load('img/bullet.png')
        #self.img.set_colorkey((0,0,0))
        self.pos = pos
        # MOVEMENT
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.imgAngle = imgAngle

    def show(self, win, rows):
        size = win.get_width() / rows
        img_copy = pygame.transform.rotate(self.img, self.imgAngle)
        win.blit(img_copy, (self.pos[0] * size - int(img_copy.get_width() / 2) , self.pos[1] * size - int(img_copy.get_height() / 2)))

    def move(self, win, mousePos, rows):
        self.pos[0] -= self.vel_x
        self.pos[1] -= self.vel_y