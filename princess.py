import pygame as pg

class Princess(pg.sprite.Sprite):
    def __init__(self, x, y):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.image = load_image('princess_idle.png', scale=0.3)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.jump = False

    def _jump(self, height, grounds):
        from main import load_image
        colisao = pg.sprite.spritecollide(self, grounds, False)
        jump_height = 19
        gravity = 1.2

        if colisao:
            self.image = load_image('princess_idle.png', scale=0.3)
            self.rect.y = colisao[0].rect.top - self.rect.height
            self.jump = False
        else:
            self.image = load_image('princess_jump.png', scale=0.3)
            if not self.jump:
                self.jump = True
                self.jump_height = -jump_height

            if self.jump:
                if self.rect.bottom >= height:
                    self.rect.y = height - self.rect.height
                    self.jump = False
                else:
                    self.rect.y += self.jump_height
                    self.jump_height += gravity