import pygame

class Bullet():

    def __init__(self, pos, vel_x, vel_y, imgAngle) -> None:
        # GRAPHICS
        self.img = pygame.image.load('img/bullet.png')
        self.imgSize = [3,10]
        # POSITIONING
        self.pos = pos
        self.rect = pygame.Rect(0,0,0,0)
        self.imgAngle = imgAngle
        # MOVEMENT
        self.vel_x = vel_x
        self.vel_y = vel_y

    def show(self, win, size):
        img_copy = pygame.transform.rotate(self.img, self.imgAngle)
        self.rect = pygame.Rect(self.pos[0] * size - int(img_copy.get_width() / 2) , self.pos[1] * size - int(img_copy.get_height() / 2), self.imgSize[0], self.imgSize[1])
        win.blit(img_copy, self.rect)

    def move(self):
        self.pos[0] -= self.vel_x / 3
        self.pos[1] -= self.vel_y / 3