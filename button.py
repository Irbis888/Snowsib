import pygame


class Button:
    def __init__(self, master, x, y, w, h, color, text):
        self.color = color
        self.rect = (x, y, w, h)
        self.master = master
        self.effect = self.master.endlevel
        self.t = text

    def render(self):
        pygame.draw.rect(self.master.screen, pygame.Color(*self.color), pygame.Rect(*self.rect))
        font = pygame.font.Font(None, 30)
        text = font.render(self.t, 1, (0, 0, 0))
        text_x = self.rect[0] + self.rect[2] / 2 - 30
        text_y = self.rect[1] + self.rect[3] / 2 - 15
        self.master.screen.blit(text, (text_x, text_y))

