import pygame

def getText(text, size, fontStyle, color, isBald=False):
    font = pygame.font.SysFont(fontStyle, size)
    rendered = font.render(text, isBald, color)
    return rendered

class Button():

    def __init__(self, text, func, bgColorPassive, bgColorActive, fontColorPassive, fontColorActive, fontSize, fontStyle) -> None:
        self.text = text
        self.func = func
        self.bg_color_passive = bgColorPassive
        self.bg_color_active = bgColorActive
        self.current_bg_color = self.bg_color_passive
        self.font_color_passive = fontColorPassive
        self.font_color_active = fontColorActive
        self.current_font_color = self.font_color_passive
        self.font_size = fontSize
        self.font_style = fontStyle

    def show(self, win, rect, mousePos, mButtonDown, player):
        pygame.draw.rect(win, self.current_bg_color, rect)
        text = getText(self.text, self.font_size, self.font_style, self.current_font_color)
        win.blit(text, [rect.left + (rect[2] - text.get_width()) / 2, rect.top + (rect[3] - text.get_height()) / 2])
        if mousePos[0] >= rect.left and mousePos[0] <= rect.right and mousePos[1] >= rect.top and mousePos[1] <= rect.bottom:
            self.current_bg_color = self.bg_color_active
            self.current_font_color = self.font_color_active
            if mButtonDown:
                if player != None:
                    self.func(player)
                else:
                    self.func()
        else:
            self.current_bg_color = self.bg_color_passive
            self.current_font_color = self.font_color_passive

