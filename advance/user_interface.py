import pygame
from button import Button
pygame.font.init()

def getText(text, size, fontStyle, color, isBald=False):
    font = pygame.font.SysFont(fontStyle, size)
    rendered = font.render(text, isBald, color)
    return rendered

class UI():
    def __init__(self, buttonRects) -> None:
        self.bg_color = (0,0,0)
        self.font_size = 15
        self.font_style = 'calibri'
        self.font_color = (255,255,255)

        self.buttons = []
        self.button_rect = pygame.Rect(buttonRects)

    def show_items(self, win, ws, txt_items):
        for i in txt_items:
            text_rect = getText(i, self.font_size, self.font_style, self.font_color)

            height = 0
            for j in txt_items[:txt_items.index(i)]:
                height += getText(j, self.font_size, self.font_style, self.font_color).get_height()

            pygame.draw.rect(win, self.bg_color, (ws[0] - text_rect.get_width(), height, text_rect.get_width(), text_rect.get_height()))
            win.blit(text_rect, (ws[0] - text_rect.get_width(), height))
    
    def show_buttons(self, win, mousePos, mButtonDown):
        for button in self.buttons:
            self.button_rect.top += self.button_rect[3] * self.buttons.index(button)
            button.show(win, self.button_rect, mousePos, mButtonDown)
        self.button_rect.top = 0
    
    def add_button(self, text, bgColorPassive, bgColorActive):
        self.buttons.append(Button(text, bgColorPassive, bgColorActive, self.font_color, self.font_size, self.font_style))