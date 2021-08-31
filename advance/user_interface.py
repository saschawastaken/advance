import pygame
pygame.font.init()

def getText(text, size, fontStyle, color, isBald=False):
    font = pygame.font.SysFont(fontStyle, size)
    rendered = font.render(text, isBald, color)
    return rendered

class Item():
    def __init__(self, text_rect, pos_y, bgColor) -> None:
        self.text_rect = text_rect
        self.pos_y = pos_y
        self.bg_color = bgColor

    def show(self, win):
        pygame.draw.rect(win, self.bg_color, (win.get_width() - self.text_rect.get_width(), self.pos_y, self.text_rect.get_width(), self.text_rect.get_height()))

class UI():

    def __init__(self, win, ) -> None:
        self.win = win 
        # FIRST ITEM
        text_rect = getText("Stats:", 15, 'calibri', (255,255,255), True)
        self.items = [Item(text_rect, win.get_height() - text_rect.get_height(), (255,0,0))]
        self.bg_color = (0,0,0)

    def show(self):
        for i in self.items:
            i.show(self.win)

    def add_item(self, text, textColor, textSize):
        text_rect = getText(text, textSize, 'calibri', textColor, False)
        self.items.append(Item(text_rect, self.items[-1].pos_y + text_rect.get_height(), self.bg_color))