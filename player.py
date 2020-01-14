import pygame
import time
from bullet import Bullet


class Player:
    def __init__(self, master, x, y):
        self.master = master
        self.vx = 0
        self.vy = 0
        self.score = 0
        self.hp = 3
        self.time = 61
        self.speed = 5
        self.shtime = time.time()
        self.dir = 90
        self.fx = 0
        self.fy = 0
        self.sprite = pygame.sprite.Sprite()
        self.image = self.master.load_image("player2.png", -1)
        rot = pygame.transform.rotate(self.image, self.dir)
        self.sprite.image = rot
        self.sprite.rect = rot.get_rect()
        self.sprite.add(self.master.gplayer)
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        self.pause = 0

    def render(self):
        self.vx = 0
        self.vy = 0
        d = self.dir
        if pygame.key.get_pressed()[112] == 1 and self.pause == 0:
            self.master.run = not self.master.run
        self.pause = pygame.key.get_pressed()[112]
        if pygame.key.get_pressed()[275] == 1:
            self.vx = self.speed
            self.dir = 0
        elif pygame.key.get_pressed()[276] == 1:
            self.vx = -self.speed
            self.dir = 180
        elif pygame.key.get_pressed()[274] == 1:
            self.vy = self.speed
            self.dir = -90
        elif pygame.key.get_pressed()[273] == 1:
            self.vy = -self.speed
            self.dir = 90
        rot = pygame.transform.rotate(self.image, self.dir)
        self.sprite.image = rot
        if self.master.run:
            self.sprite.rect.x += self.vx
            self.sprite.rect.y += self.vy
            self.fx += self.vx
            self.fy += self.vy
            self.time -= 0.02
        if pygame.sprite.spritecollideany(self.sprite, self.master.gw):
            self.sprite.rect.x -= self.vx
            self.sprite.rect.y -= self.vy
            self.fx -= self.vx
            self.fy -= self.vy
        if d != self.dir and self.dir in (90, -90) and d in (0, 180):
            if abs(self.fx) > 12:
                if self.fx > 0:
                    self.sprite.rect.x += 25 - abs(self.fx)
                else:
                    self.sprite.rect.x -= 25 - abs(self.fx)
                self.fx = 0
            else:
                if self.fx > 0:
                    self.sprite.rect.x -= abs(self.fx)
                else:
                    self.sprite.rect.x += abs(self.fx)
                self.fx = 0
        elif d != self.dir:
            if abs(self.fy) > 12:
                if self.fy > 0:
                    self.sprite.rect.y += 25 - abs(self.fy)
                else:
                    self.sprite.rect.y -= 25 - abs(self.fy)
                self.fy = 0
            else:
                if self.fy > 0:
                    self.sprite.rect.y -= abs(self.fy)
                else:
                    self.sprite.rect.y += abs(self.fy)
                self.fy = 0
        if abs(self.fx) >= 25:
            self.fx = 0
        if abs(self.fy) >= 25:
            self.fy = 0
        if pygame.sprite.spritecollide(self.sprite, self.master.gs, False):
            self.score += len(pygame.sprite.spritecollide(self.sprite, self.master.gs, True))

        if self.time <= 0 or self.hp <= 0:
            self.master.gameover()
        if self.score == self.master.sc + 3 * len(self.master.slist):
            self.master.endlevel()
        if pygame.key.get_pressed()[32] == 1 and self.master.run:
            if time.time() - self.shtime >= 0.5:
                self.shoot()
                self.shtime = time.time()
        for j in pygame.sprite.spritecollide(self.sprite, self.master.gb, False):
            for i in self.master.blist:
                if j == i.sprite and i.snowman:
                    self.hp -= 1
                    j.kill()

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
        self.master.blist.append(b)
