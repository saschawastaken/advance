import pygame

class Bullet():

    def __init__(self, pos, vel_x, vel_y) -> None:
        # GRAPHICS
        self.color = (255,255,0)
        self.pos = pos
        # MOVEMENT
        self.vel_x = vel_x
        self.vel_y = vel_y

    def show(self, win, rows):
        size = win.get_width() / rows
        pygame.draw.rect(win, self.color, (self.pos[0] * size, self.pos[1] * size, size, size))

    def move(self):
        self.pos[0] -= self.vel_x
        self.pos[1] -= self.vel_y