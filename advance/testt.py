import pygame

pygame.font.init()
pygame.display.init()

win = pygame.display.set_mode([500,500])

globalFontSize = 15
globalFont = pygame.font.SysFont('calibri', globalFontSize)
text = globalFont.render('kek', False, (255,0,0))

space = win.get_width() * 0.02
win.blit(text, (win.get_width() - text.get_rect()[2] - space, space))


pygame.display.update()
while True: pass