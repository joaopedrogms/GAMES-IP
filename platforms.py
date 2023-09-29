import pygame as pg

#classe das plataformas com iniclização de sprite personalizado
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width=0, height=0, sprite=0):
        pg.sprite.Sprite.__init__(self)
        from main import load_image
        if sprite == 0:
            self.image = pg.Surface((width, height), pg.SRCALPHA)
            self.rect = pg.Rect(x, y, width, height)
        else:
            self.image = load_image('sprite_platform_'+str(sprite)+'.png', scale=1.3)
            self.rect = pg.Rect(x, y, self.image.get_width(), 1)