import pygame as pg

class Princess(pg.sprite.Sprite):
    def __init__(self, x, y):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.image = load_image('princess_idle.png', scale=0.3)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.jumping = False
        self.jumping_height = -19.3
        self.gravity = 1
        self.vertical_speed = 0
        self.on_ground = False

    def update(self, plataforms_group):
        self._gravity(plataforms_group)
        self._jump()
        self._animation()

    def _jump(self):
        if self.on_ground and not self.jumping:
            self.vertical_speed = self.jumping_height
            self.jumping = True

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

    def _animation(self):
        from main import load_image
        if self.jumping:
            self.image = load_image('princess_jump.png')
        else:
            self.image = load_image('princess_idle.png')
