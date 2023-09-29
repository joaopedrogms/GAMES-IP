import pygame as pg
from pygame.locals import *
from main import *

#classe do personagem controlável pelo jogador 
class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = load_image('main_character_idle.png')
        self.rect = load_image('main_character_idle.png').get_rect()

        self.hp = 3
        self.new_hp = 0
        self.attack = 1
        self.speed = 6

        self.yellow_keys_collected = 0
        self.blue_keys_collected = 0
        self.cage_collected = False
        self.can_jump = False
        self.strawberries_collected = 0

        self.rect.bottomleft = (0, 300)

        self.looking_right = True
        self.jumping = False

        self.jumping_height = -19.4
        self.gravity = 1
        self.vertical_speed = 0
        self.on_ground = False

    def update(self, width, platforms_group):
        self._gravity(platforms_group)
        self._jump()
        self._walk(width)
        self._animation()

        if self.strawberries_collected >= 10:
            self.hp += 1
            self.new_hp += 1
            self.strawberries_collected -= 10

    #jump do personagem
    def _jump(self):
        up_pressed = pg.key.get_pressed()[pg.K_UP]
        w_pressed = pg.key.get_pressed()[pg.K_w]

        if not self.cage_collected:
            if (up_pressed or w_pressed) and self.on_ground and not self.jumping:
                self.vertical_speed = self.jumping_height
                self.jumping = True
        else:
            if self.can_jump and self.on_ground and not self.jumping:
                self.vertical_speed = self.jumping_height
                self.jumping = True

    #movimento do personagem
    def _walk(self, width):
        d_pressed = pg.key.get_pressed()[pg.K_d]
        right_pressed = pg.key.get_pressed()[pg.K_RIGHT]
        left_pressed = pg.key.get_pressed()[pg.K_LEFT]
        a_pressed = pg.key.get_pressed()[pg.K_a]

        if not self.cage_collected:
            if d_pressed or right_pressed:
                self.looking_right = True
                if self.rect.right < width:
                    self.rect = self.rect.move(self.speed, 0)
            elif left_pressed or a_pressed:
                self.looking_right = False
                if self.rect.left > 0:
                    self.rect = self.rect.move(-self.speed, 0)

    #animação do personagem
    def _animation(self):
        if self.jumping:
            if self.looking_right:
                self.image = pg.transform.flip(load_image('main_character_jump.png'), True, False)
            else:
                self.image = load_image('main_character_jump.png')
        else:
            if self.looking_right:
                self.image = pg.transform.flip(load_image('main_character_idle.png'), True, False)
            else:
                self.image = load_image('main_character_idle.png')

    #checgaem de gravidadedo pulo
    def _gravity(self, platforms_group):
        previous_y = self.rect.y
        self.rect = self.rect.move(0, self.vertical_speed)
        self.on_ground = bool(pg.sprite.spritecollide(self, platforms_group, False))

        if self.on_ground:
            self.rect.y = previous_y
            self.vertical_speed = 0
            self.jumping = False
        else:
            self.vertical_speed += self.gravity