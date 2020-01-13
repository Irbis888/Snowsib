import pygame


class Bullet:
    def __init__(self, master, x, y):
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.image = self.master.load_image("carrot.png", (255, 255, 255))
        self.sprite.rect = self.image.get_rect()
        self.sprite.add(self.master.gb)
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        self.snowman = False
        self.vx = 0
        self.vy = 0
        self.dir = 0

    def render(self):
        self.sprite.rect.x += self.vx
        self.sprite.rect.y += self.vy
        for i in pygame.sprite.spritecollide(self.sprite, self.master.gw, False):
            for j in self.master.wlist:
                if i == j.sprite:
                    if j.breakable:
                        if j.damaged:
                            i.kill()
                        else:
                            if self.dir in (0, 180):
                                i.image = self.master.load_image("wall4.png")
                                x = i.rect.x
                                y = i.rect.y
                                i.rect = i.image.get_rect()
                                i.rect.x = x
                                i.rect.y = y
                                if self.dir == 0:
                                    i.rect.x += 25
                            else:
                                i.image = self.master.load_image("wall3.png")
                                x = i.rect.x
                                y = i.rect.y
                                i.rect = i.image.get_rect()
                                i.rect.x = x
                                i.rect.y = y
                                if self.dir == -90:
                                    i.rect.y += 25
                            j.damaged = True
            self.sprite.kill()
            self.render = lambda: print(end="")
        if pygame.sprite.spritecollideany(self.sprite, self.master.gsm) and not self.snowman:
            for i in pygame.sprite.spritecollide(self.sprite, self.master.gsm, False):
                for j in self.master.slist:
                    if j.sprite == i:
                        j.render = lambda: print(end="")
            self.sprite.kill()
            self.render = lambda: print(end="")
            self.master.player.score += 3 * len(pygame.sprite.spritecollide(self.sprite, self.master.gsm, True))
        for i in pygame.sprite.spritecollide(self.sprite, self.master.gb, False):
            for j in self.master.blist:
                if j.sprite == i and j.snowman != self.snowman:
                    i.kill()
                    j.render = lambda: print(end="")
                    self.sprite.kill()
                    self.render = lambda: print(end="")

