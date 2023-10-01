import sys
import pygame as pg
from pygame.locals import *
from main import *

#classe do personagem controlável pelo jogador 
class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = load_image('main_character_idle.png')
        self.rect = self.image.get_rect()

        self.hp = 1
        self.new_hp = 0
        self.attack = 1
        self.speed = 6

        self.golden_keys_collected = 0
        self.silver_keys_collected = 0
        self.cage_collected = False
        self.can_jump = False
        self.strawberries_collected = 0

        self.rect.bottomleft = (0, 687)

        self.looking_right = True
        self.jumping = False

        self.jumping_height = -19.4
        self.gravity = 1
        self.vertical_speed = 0
        self.horizontal_speed = 0
        self.on_ground = False

    def update(self, width, platforms_group):
        self._gravity(platforms_group)
        self._jump()
        self._walk(width)
        self._animation()
        self._death()
        self._strawberry()

    #jump do personagem
    def _jump(self):
        up_pressed = pg.key.get_pressed()[pg.K_UP]
        w_pressed = pg.key.get_pressed()[pg.K_w]
        space_pressed = pg.key.get_pressed()[pg.K_SPACE]

        if not self.cage_collected:
            if (up_pressed or w_pressed or space_pressed) and self.on_ground and not self.jumping:
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
                self.horizontal_speed = self.speed

                if self.rect.right < width:
                    self.rect = self.rect.move(self.horizontal_speed, 0)

            elif left_pressed or a_pressed:
                self.looking_right = False
                self.horizontal_speed = -self.speed

                if self.rect.left > 0:
                    self.rect = self.rect.move(self.horizontal_speed, 0)

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

    #checgaem de gravidade do pulo e se a plataforma esta em cima ou embaixo do personagem
    def _gravity(self, platforms_group):
        self.rect = self.rect.move(0, self.vertical_speed)
        self.on_ground = False

        for platform in platforms_group:
            if self.rect.colliderect(platform.rect):
                # personagem caindo e checagem de colisao lateral
                if self.rect.bottom - (platform.rect.top + self.vertical_speed) <= 0:
                    self.rect.y = platform.rect.y - self.rect.height
                    self.vertical_speed = 0
                    self.on_ground = True
                    self.jumping = False
                #personagem subindo e checagem de colisao lateral
                elif self.rect.top - (platform.rect.bottom + self.vertical_speed) > 0:
                    self.rect.y = platform.rect.y + platform.rect.height
                    self.vertical_speed = 0
                else:
                    #checagem colisao plataformas
                    if self.horizontal_speed > 0:
                        self.rect.right = platform.rect.left
                    elif self.horizontal_speed < 0:
                        self.rect.left = platform.rect.right

        if not self.on_ground:
            self.vertical_speed += self.gravity

    def _strawberry(self):
        if self.strawberries_collected >= 10:
            self.new_hp += 1
            self.strawberries_collected -= 10
            if self.hp < 5:
                self.hp += 1

    def _death(self):
        if self.rect.y > 900:
            if self.hp > 1:
                self.hp -= 1
                self.rect.bottomleft = (0, 687)
                self.looking_right = True
                self.vertical_speed = 0
                self.on_ground = False
                self.jumping = False
                self.can_jump = False
            else:
                self.hp = 0
                sys.exit()