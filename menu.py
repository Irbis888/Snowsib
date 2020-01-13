import pygame


class Menu:
    def __init__(self, master, x, y):
        self.master = master
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.master.load_image("menu.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.add(self.master.other)
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def render(self):
        font = pygame.font.Font(None, 30)
        text = font.render("Осталось времени:", 1, (0, 0, 0))
        text_x = 1100
        text_y = 25
        self.master.screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 100)
        text = font.render(str(self.master.player.hp), 1, (0, 0, 0))
        text_x = 1250
        text_y = 370
        self.master.screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 30)
        text = font.render("Очки:", 1, (0, 0, 0))
        text_x = 1100
        text_y = 500
        self.master.screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 60)
        text = font.render(str(self.master.player.score), 1, (0, 0, 0))
        text_x = 1100
        text_y = 550
        self.master.screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 60)
        t = self.master.player.time
        text = font.render(str(int(t // 60)) + ":" + (str(int(t % 60)) if len(str(int(t % 60))) == 2 else
                                                      "0" + str(int(t % 60))), 1, (0, 0, 0))
        text_x = 1170
        text_y = 140
        self.master.screen.blit(text, (text_x, text_y))
