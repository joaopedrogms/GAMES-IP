import pygame as pg

#classe da princesa do jogo
class Princess(pg.sprite.Sprite):
    def __init__(self, x, y):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.image = load_image('princess_idle.png', scale=0.3)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.jumping = False
        self.can_jump = False
        self.jumping_height = -19.3
        self.gravity = 1
        self.vertical_speed = 0
        self.on_ground = False
        self.jump_count = 0

    #atualização da gravidade, pulo e animação
    def update(self, plataforms_group):
        self._gravity(plataforms_group)
        self._jump()
        self._animation()

    def _jump(self):
        if self.on_ground and self.can_jump and not self.jumping:
            self.vertical_speed = self.jumping_height
            self.jumping = True
            self.jump_count += 1

    def _gravity(self, platforms_group):
        self.rect = self.rect.move(0, self.vertical_speed)
        self.on_ground = False

        for platform in platforms_group:
            if self.rect.colliderect(platform.rect):
                # personagem caindo e checagem de colisao lateral
                if self.vertical_speed >= 0:
                    self.rect.y = platform.rect.y - self.rect.height
                    self.vertical_speed = 0
                    self.on_ground = True
                    self.jumping = False
                # personagem subindo e checagem de colisao lateral
                elif self.vertical_speed < 0:
                    self.rect.y = platform.rect.y + platform.rect.height
                    self.vertical_speed = 0

        if not self.on_ground:
            self.vertical_speed += self.gravity

    def _animation(self):
        from main import load_image
        if self.jumping:
            self.image = load_image('princess_jump.png')
        else:
            self.image = load_image('princess_idle.png')
