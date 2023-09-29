import pygame as pg

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.image.fill((0, 0, 0, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)