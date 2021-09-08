import pygame
from random import randint
class Tile():
    def __init__(self, pos) -> None:
        self.pos = pos
        self.color = (139,69,19)
        self.lifetime = randint(10, 10)

    def show(self, win, size):
        pygame.draw.rect(win, self.color, (self.pos[0] * size, self.pos[1] * size, size, size))