import pygame as pg

class Hole(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill((101, 155, 255))
        self.rect = (x, y)