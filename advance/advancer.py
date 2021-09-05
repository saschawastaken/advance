import pygame
from random import randint

class Advancer():

    def __init__(self, rows) -> None:
        # MOVEMENT
        self.path = [[randint(0, rows - 1), 0]]
        self.movementLog = [0]
        # GRAPHICAL ELEMENTS
        self.color = (128,0,255)

    def show(self, win, size):
        for i in self.path[:-1]:
            pygame.draw.rect(win, self.color, (i[0] * size + 1, i[1] * size + 1, size - 1, size - 1))
        pygame.draw.rect(win, (255,0,0), (self.path[-1][0] * size, self.path[-1][1] * size, size, size))
        
    def move(self, pTiles, enemys, rows):
        if randint (0, 100) == 0:
            direction_y = randint(0, 1)

            last_pos = self.path[-1].copy()

            if direction_y == 0:
                last_pos[0] += randint(-1, 1)
            else:
                last_pos[1] += direction_y

            collision_check = True
            for t in pTiles:
                if last_pos == t.pos:
                    collision_check = False
            for a in enemys:
                for p in a.path:
                    if last_pos == p:
                        collision_check = False

            if collision_check and last_pos[0] > 0 and last_pos[0] < rows:
                self.path.append(last_pos)
