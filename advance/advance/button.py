import pygame

class Button():

    def __init__(self, rect, color, fontStyle) -> None:
        # GRAPHICALS
        self.rect = rect
        self.color = color
        self.fontStyle = fontStyle

    def show(self, win):
        pygame.draw.rect(win, self.color, self.rect)

