import pygame

class Tile():

    def __init__(self, sP, eP) -> None:
        self.startPos = sP
        self.endPos = eP
        self.color = (139,69,19)

    def show(self, win, size):
        currentPos = self.startPos
        while currentPos != self.endPos:
            pygame.draw.rect(win, self.color, (currentPos[0] * size, currentPos[1] * size, size, size))
            currentPos[0] += 1