import pygame
import os
from wall import Wall
from snow import Snow
from snowman import Snowman
from player import Player
from menu import Menu
from base import Base


class Level:
    def __init__(self, master, screen, wallist, brwalls, snowlist, snowmanlist, player, base):
        self.screen = screen
        self.master = master
        self.gplayer = pygame.sprite.Group()
        self.gsm = pygame.sprite.Group()
        self.gs = pygame.sprite.Group()
        self.gw = pygame.sprite.Group()
        self.gb = pygame.sprite.Group()
        self.gbase = pygame.sprite.Group()
        self.other = pygame.sprite.Group()
        self.btnlist = []
        self.base = Base(self, *base)
        self.run = True
        self.slist = []
        self.blist = []
        self.wlist = []
        self.sc = 0
        for i in wallist:
            self.wlist.append(Wall(self, i[1] * 50, i[0] * 50))
        for i in brwalls:
            w = Wall(self, i[1] * 50, i[0] * 50)
            w.breakable = True
            w.sprite.image = self.load_image("wall2.png")
            self.wlist.append(w)
        for i in snowlist:
            Snow(self, i[1] * 50, i[0] * 50)
            self.sc += 1
        for i in snowmanlist:
             self.slist.append(Snowman(self, i[1] * 50, i[0] * 50))
        self.player = Player(self, *player[:-1])
        self.player.time = player[-1]
        for i in range(30):
            Wall(self, i * 50, -50)
            Wall(self, i * 50, 750)
            Wall(self, -50, i * 50)
            Wall(self, 1050, i * 50)
        self.menu = Menu(self, 1050, 0)

    def render(self):
        pass

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('pics', name)
        image = pygame.image.load(fullname).convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def gameover(self):
        self.run = False

    def endlevel(self):
        self.run = False
        self.master.time = self.player.time
        if self.master.guess + 1 < len(self.master.levels):
            self.master.guess += 1
        else:
            self.master.guess = 0
