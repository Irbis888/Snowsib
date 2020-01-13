import pygame


class Snow:
    def __init__(self, master, x, y):
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.master.load_image("whitecircle.png", -1)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.add(self.master.gs)
        self.sprite.rect.x = x
        self.sprite.rect.y = y

