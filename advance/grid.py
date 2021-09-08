import pygame

class Grid():

    def __init__(self, rows, ws) -> None:
        self.rows = rows
        self.size = ws[0] / self.rows
        self.color = (64,64,64)

    def show(self, win, ws):
        # VERTIKAL
        for i in range(self.rows + 1):
            pygame.draw.line(win, self.color, (0, ws[1] * i/self.rows), (ws[0], ws[1] * i/self.rows))
        pygame.draw.line(win, self.color, (0, ws[1] - 1), (ws[0], ws[1] - 1))
        # HORIZONTAL
        for j in range(self.rows + 1):
            pygame.draw.line(win, self.color, (ws[0] * j/self.rows, 0), (ws[0] * j/self.rows, ws[1]))
               