import pygame


class Base:
    def __init__(self, master, x, y):
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.master.load_image("pine.png", -1)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.add(self.master.gbase)
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def render(self):
        if pygame.sprite.spritecollide(self.sprite, self.master.gb, True):
            self.sprite.kill()
            self.master.gameover()
