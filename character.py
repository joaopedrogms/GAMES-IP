import pygame as pg
from pygame.locals import *
from main import *

#classe do personagem controlável pelo jogador 
class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image('sprite_llama.png')
        self.rect = load_image('sprite_llama.png').get_rect()
        self.image_upper = self.rect.copy()
        self.looking = True
        self.jump = False
        self.can_jump = True
        self.hp = 3
        self.new_hp = 0
        self.attack = 1
        self.speed = 3
        self.yellow_keys_collected = 0
        self.blue_keys_collected = 0
        self.cage_collected = False
        self.strawberries_collected = 0
        self.rect.bottomleft = (0, 687)
        self.cameraX = 0
        self.cameraY = 0

    def update(self, width, height, grounds):
        top_value = self.rect[1]
        if top_value == 0:
            self.rect = self.rect.move(
                0, pg.display.get_surface().get_size()[1] - self.rect[3])
            self.image_upper = self.rect.copy()

        if self.strawberries_collected >= 10:
            self.hp += 1
            self.new_hp += 1
            self.strawberries_collected -= 10

        self.animation()
        if not self.cage_collected:
            self._walk(width)
        if self.can_jump:
            self._jump(height, pg.sprite.spritecollide(self, grounds, False))

    # jump
    def _jump(self, height, colisao):
        if self.cage_collected:
            up_pressed = True
            w_pressed = True
        else:
            up_pressed = pg.key.get_pressed()[pg.K_UP]
            w_pressed = pg.key.get_pressed()[pg.K_w]
        jump_height = 10
        gravity = 0.3

        #observa se o personagem está colidindo com o chão ou pulando
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

    #movimento do personagem
    def _walk(self, width):
        d_pressed = pg.key.get_pressed()[pg.K_d]
        right_pressed = pg.key.get_pressed()[pg.K_RIGHT]
        left_pressed = pg.key.get_pressed()[pg.K_LEFT]
        a_pressed = pg.key.get_pressed()[pg.K_a]

        if d_pressed or right_pressed:
            self.looking = True
            if self.rect.right >= width and self.cameraX < 1080:
                self.cameraX += self.speed
            if self.rect.right <= width:
                self.rect = self.rect.move(self.speed, 0)
        elif left_pressed or a_pressed:
            self.looking = False
            if self.rect.left > 0:
                self.rect = self.rect.move(-self.speed, 0)
            if self.rect.left <= 0 and self.cameraX > 0:
                self.cameraX -= self.speed    

    #animação do personagem
    def animation(self):
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