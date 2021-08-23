import pygame

class Grid():

    def __init__(self, rows, win) -> None:
        self.rows = rows
        self.size = win.get_width() / self.rows
        self.color = (64,64,64)

    def show(self, win):
        # VERTIKAL
        for i in range(self.rows + 1):
            pygame.draw.line(win, self.color, (0, win.get_height() * i/self.rows), (win.get_width(), win.get_height() * i/self.rows))
        pygame.draw.line(win, self.color, (0, win.get_height() - 1), (win.get_width(), win.get_height() - 1))
        # HORIZONTAL
        for j in range(self.rows + 1):
            pygame.draw.line(win, self.color, (win.get_width() * j/self.rows, 0), (win.get_width() * j/self.rows, win.get_height()))
        pygame.draw.line(win, self.color, (win.get_width() - 1, 0), (win.get_width() - 1, win.get_height()))
               