import pygame as pg
from pygame.locals import *
from main import *

class Character(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image('sprite_llama.png')
        self.rect = load_image('sprite_llama.png').get_rect()
        self.image_upper = self.rect.copy()
        self.looking = True
        self.jump = False
        self.hp = 3
        self.vidas_adicionadas = 0
        self.attack = 1
        self.speed = 3
        self.yellow_keys_collected = 0
        self.blue_keys_collected = 0
        self.jaula_coletada = False
        self.strawberries_collected = 0

    def update(self, width, height, grounds):
        top_value = self.rect[1]
        if top_value == 0:
            self.rect = self.rect.move(
                0, pg.display.get_surface().get_size()[1] - self.rect[3])
            self.image_upper = self.rect.copy()

        if self.strawberries_collected >= 10:
            self.hp += 1
            self.vidas_adicionadas += 1
            self.strawberries_collected -= 10

        self._walk(width)
        colisao_chao = pg.sprite.spritecollide(self, grounds, False)
        self._jump(height, colisao_chao)

    def _jump(self, height, colisao):
        up_pressed = pg.key.get_pressed()[pg.K_UP]
        w_pressed = pg.key.get_pressed()[pg.K_w]
        jump_height = 10
        gravity = 0.3

        if colisao:
            self.rect.y = colisao[0].rect.top - self.rect.height
            self.jump = False
        else:
            if (w_pressed or up_pressed) and not self.jump:
                self.jump = True
                self.jump_height = -jump_height

            if self.jump:
                if self.rect.bottom >= height:
                    self.rect.y = height - self.rect.height
                    self.jump = False
                else:
                    self.rect.y += self.jump_height
                    self.jump_height += gravity

    def _walk(self, width):
        d_pressed = pg.key.get_pressed()[pg.K_d]
        right_pressed = pg.key.get_pressed()[pg.K_RIGHT]
        left_pressed = pg.key.get_pressed()[pg.K_LEFT]
        a_pressed = pg.key.get_pressed()[pg.K_a]

        if d_pressed or right_pressed:
            self.looking = True
            if self.rect.right < width:
                self.rect = self.rect.move(self.speed, 0)
        elif left_pressed or a_pressed:
            self.looking = False
            if self.rect.left > 0:
                self.rect = self.rect.move(-self.speed, 0)

        if self.jump:
            if self.looking:
                self.image = pg.transform.flip(load_image('sprite_llama_pulo.png'), True, False)
            else:
                self.image = load_image('sprite_llama_pulo.png')
        else:
            if self.looking:
                self.image = pg.transform.flip(load_image('sprite_llama.png'), True, False)
            else:
                self.image = load_image('sprite_llama.png')

