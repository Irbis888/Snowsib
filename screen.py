import pygame
from level import Level
from button import Button


class Screen(Level):
    def __init__(self, master, screen, text, *btns):
        super().__init__(master, screen, [], [], [], [], (0, 0, 999999), (0, 0))
        self.player.render = lambda: print(end="")
        self.run = False
        eflist = [self.endlevel, lambda: self.master.exit()]
        c = -1
        for i in btns:
            c += 1
            b = Button(self, *i)
            b.effect = eflist[c if c < len(eflist) else 0]
            self.btnlist.append(b)
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.load_image("inter.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.add(self.other)
        self.sprite.rect.x = 0
        self.sprite.rect.y = 0
        self.t = text

    def render(self):
        for i in self.btnlist:
            i.render()
        for i in self.t:
            font = pygame.font.Font(None, 30)
            text = font.render(i[0], 1, i[3])
            text_x = i[1]
            text_y = i[2]
            self.screen.blit(text, (text_x, text_y))






