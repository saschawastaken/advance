import pygame
from pygame.locals import *
from user_interface import UI
from random import *

run = True

def menu():
    global title_text
    win = pygame.display.set_mode([500,500])
    pygame.display.set_caption("")
    pygame.display.set_icon(pygame.image.load("img/none.png"))
    clock = pygame.time.Clock()
    tps = 60

    def getText(text, size, fontStyle, color, isBald=False):
        font = pygame.font.SysFont(fontStyle, size)
        rendered = font.render(text, isBald, color)
        return rendered

    title_text = "Advancer"
    title = getText(title_text, 30, 'gillsansultracondensed', (255,255,255), True)

    class Snake():

        def __init__(self) -> None:
            self.size = 10
            self.color = (255,0,0)
            self.body = [[randint(0, win.get_width() / self.size), randint(0, win.get_height() / self.size)]]
            self.direction = [1, 0]
            self.moving_counter = 0
            self.g_body = pygame.image.load("img/a_body.png").convert()
            self.g_head = pygame.image.load("img/a_head.png").convert()

        def show(self, win):
            for body in self.body[:-1]:
                win.blit(self.g_body, (body[0] * self.size, body[1] * self.size, self.size, self.size))
            win.blit(self.g_head, (self.body[-1][0] * self.size, self.body[-1][1] * self.size, self.size, self.size))            

        def move(self):
            reset = False
            appending = randint(0, 1) == 0
            new_body = []
            collision_check = False
            count_to_resettment = 0

            while not collision_check:
                count_to_resettment += 1
                if count_to_resettment > 5000:
                    reset = True
                    break
                
                last_dir = self.direction

                while self.direction == last_dir:
                    self.direction = [0, 0]
                    self.direction[randint(0,1)] = choice([-1, 1])

                new_body = [self.body[-1].copy()[0] + self.direction[0], self.body[-1].copy()[1] + self.direction[1]]
                collision_check = True
                
                for body in self.body:
                    if body == new_body:
                        collision_check = False

            self.body.append(new_body)

            if not appending:
                self.body.pop(0)

            if self.body[-1][0] < 0 or self.body[-1][0] >= win.get_width() / self.size or self.body[-1][1] < 0 or self.body[-1][1] >= win.get_height() / self.size or reset:
                pass

    def bStart():
        global run
        run = False
    def bQuit():
        quit(0)

    bWidth = 100
    bHeight = 50

    ui = UI([win.get_width() / 2 - bWidth / 2, win.get_height() / 2 - bHeight / 2, bWidth, bHeight], 10)
    ui.add_button("Start", bStart, (200,200,200), (0,100,0), (0,0,0), (255,255,255))
    ui.add_button("Quit", bQuit, (200,200,200), (100,0,0), (0,0,0), (255,255,255))

    s = Snake()

    mouseButtonDown = False

    while run:
        clock.tick(tps)
        mouseButtonDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseButtonDown = True

        win.fill((0,0,10))
        s.show(win)
        if s.moving_counter == tps:
            s.move()
            s.moving_counter = 0
        s.moving_counter += 1
        ui.show_items(win, [win.get_width(), win.get_height], pygame.mouse.get_pos(), mouseButtonDown, [])
        title = getText(title_text, 30, 'gillsansultracondensed', (255,255,255), True)
        win.blit(title, (win.get_width() / 2 - title.get_width() / 2, win.get_height() * 0.3, title.get_width(), title.get_height()))
        pygame.display.update()