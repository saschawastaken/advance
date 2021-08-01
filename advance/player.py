import pygame

class Player():

    def __init__(self, pos, imgURL) -> None:
        # *Key elements marked with k at beginning
        self.pos = pos
        # GRAPHICAL
        self.img = pygame.image.load(imgURL)
        self.color = (0,255,0)
        # MOVEMENT (Key elements marked with k at beginning)
        self.kShoot = False
        # BUILD ACTION
        self.kBuildMode = False
        
    def show(self, win, rows):
        size = win.get_width() / rows
        #pygame.draw.rect(win, self.color, (self.pos[0] * size + 1, self.pos[1] * size + 1, size -1, size - 1))
        win.blit(self.img, (self.pos[0] * size , self.pos[1] * size, size, size))

    def shoot(self):
        if self.kShoot:
            pass

    def build(self):
        pass