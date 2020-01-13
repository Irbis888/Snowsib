import pygame
import random
from bullet import Bullet


class Snowman:
    def __init__(self, master, x, y):
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.dir = 0
        self.speed = 5
        self.image = self.master.load_image("snowman.png", -1)
        rot = pygame.transform.rotate(self.image, self.dir)
        self.sprite.image = rot
        self.sprite.rect = rot.get_rect()
        self.sprite.add(self.master.gsm)
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        self.vx = 10
        self.vy = 0
        self.count = 0

    def render(self):
        self.sprite.rect.x += self.vx
        self.sprite.rect.y += self.vy
        if pygame.sprite.spritecollideany(self.sprite, self.master.gw):
            self.sprite.rect.x -= self.vx
            self.sprite.rect.y -= self.vy
            r = random.randint(0, 4)
            if r == 0:
                self.vx = self.speed
                self.vy = 0
                self.dir = 0
            if r == 1:
                self.vy = -self.speed
                self.vx = 0
                self.dir = 90
            if r == 2:
                self.vx = -self.speed
                self.vy = 0
                self.dir = 180
            if r == 3:
                self.vy = self.speed
                self.vx = 0
                self.dir = -90
            if self.dir == 180:
                rot = pygame.transform.flip(self.image, True, False)
            else:
                rot = pygame.transform.rotate(self.image, self.dir)
            self.sprite.image = rot
        self.count += 0.01
        if self.count >= 1:
            self.shoot()
            self.count = 0

    def shoot(self):
        x = self.sprite.rect.x
        y = self.sprite.rect.y
        b = Bullet(self.master, x, y)
        if self.dir == 0:
            b.vx = self.speed * 5
            x = self.sprite.rect.x
            y = self.sprite.rect.y + 17
        if self.dir == 90:
            b.vy = self.speed * -5
            x = self.sprite.rect.x + 17
            y = self.sprite.rect.y
        if self.dir == 180:
            b.vx = self.speed * -5
            x = self.sprite.rect.x
            y = self.sprite.rect.y + 17
        if self.dir == -90:
            b.vy = self.speed * 5
            x = self.sprite.rect.x + 17
            y = self.sprite.rect.y
        rot = pygame.transform.rotate(b.image, self.dir)
        b.sprite.image = rot
        b.sprite.rect = b.sprite.image.get_rect()
        b.sprite.rect.x = x
        b.sprite.rect.y = y
        b.dir = self.dir
        b.snowman = True
        self.master.blist.append(b)
