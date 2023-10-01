import pygame as pg

class Cloud(pg.sprite.Sprite):
    def __init__(self, x, y, sprite):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.flip(load_image(sprite, scale=3), False, True)
        self.image.set_alpha(204)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self):
        self.rect = self.rect.move(self.speed, 0)
        if self.rect.left > 2214:
            self.rect.right = 0