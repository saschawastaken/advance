import pygame
from random import randint

class Advancer():

    def __init__(self) -> None:
        # MOVEMENT
        self.path = [[10, 0]]
        self.movementLog = [0]
        # GRAPHICAL ELEMENTS
        self.color = (128,0,255)

    def show(self, win, size):
        for i in self.path:
            pygame.draw.rect(win, self.color, (i[0] * size + 1, i[1] * size + 1, size - 1, size - 1))
        pygame.draw.rect(win, (0,0,0))

    def move(self, rows, pTiles):
        if 0 == randint(0,4):
            direction = randint(-1, 1)
            toChange = self.path[-1]

            # LEFT
            if direction == -1 and self.path[-1][0] > 0 and self.movementLog[-1] != 1:
                toChange[0] += direction
            # RIGHT
            elif direction == 1 and self.path[-1][0] < rows and self.movementLog[-1] != -1:
                toChange[0] += direction
            # DOWN
            else:
                toChange[1] += 1

            """
            noCollision = True
            for t in pTiles:
                if 
            """
            self.path.append([0,0])
            self.path[-1][0] = toChange[0]
            self.path[-1][1] = toChange[1]
            self.movementLog.append(direction)