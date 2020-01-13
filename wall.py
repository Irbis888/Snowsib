import pygame


class Wall:
    def __init__(self, master, x, y):
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.breakable = False
        self.damaged = False
        self.sprite.image = self.master.load_image("wall.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.add(self.master.gw)
        self.sprite.rect.x = x
        self.sprite.rect.y = y

