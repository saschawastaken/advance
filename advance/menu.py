import pygame
from pygame.locals import *
from user_interface import UI
win = pygame.display.set_mode([500,500])

clock = pygame.time.Clock()
tps = 60

def bStart():
    pass

ui = UI([100, 100, 50, 20])


ui.add_button("Start", bStart, (200,200,200), (0,255,0))
mouseButtonDown = False

while True:
    clock.tick(tps)
    mouseButtonDown = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseButtonDown = True

    win.fill((0,0,0))
    ui.show_items(win, [win.get_width(), win.get_height], pygame.mouse.get_pos(), mouseButtonDown, [], None)
    pygame.display.update()

if __name__ == "__main__":
    print("TRUE")