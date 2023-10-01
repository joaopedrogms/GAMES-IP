import pygame as pg
from collectables import *

class HUD(pg.sprite.Sprite):
    def __init__(self, character):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.character = character
        self.heart_image = load_image('heart.png', scale=0.05)
        self.yellow_key_image = load_image('yellow_key.png', scale=0.05)
        self.blue_key_image = load_image('blue_key.png', scale=0.05)
        self.strawberry_image = load_image('strawberry.png', scale=0.149)
        self.rect = self.heart_image.get_rect()
        self.rect.topleft = (10, 10)
        try:
            self.key_font = pg.font.Font('media/font/daydream.ttf', 15)

        except:
            self.key_font = pg.font.Font(None, 30)

    def update(self):
        self.image = pg.Surface((1900, 1900), pg.SRCALPHA)

        # hearts
        heart_x = 10
        for _ in range(self.character.hp):
            self.image.blit(self.heart_image, (heart_x, 10))
            heart_x += 35

        # strawberries
        strawberry_rect = self.strawberry_image.get_rect()
        strawberry_rect.topleft = (self.image.get_width() - 946, 10)
        self.image.blit(self.strawberry_image, strawberry_rect)
        strawberry_count = self.key_font.render(str(self.character.strawberries_collected + (self.character.new_hp * 10)), True, (196, 0, 40))
        self.image.blit(strawberry_count, (strawberry_rect.right + 10, (strawberry_rect.centery - strawberry_count.get_height() // 2) + 5))

        # yellow keys
        yellow_key_rect = self.yellow_key_image.get_rect()
        yellow_key_rect.topleft = (self.image.get_width() - 946, 56)
        self.image.blit(self.yellow_key_image, yellow_key_rect)
        yellow_key_count = self.key_font.render(str(self.character.yellow_keys_collected) + ' / 2', True, (255, 255, 160))
        self.image.blit(yellow_key_count, (
        yellow_key_rect.right + 10, yellow_key_rect.centery - yellow_key_count.get_height() // 2))

        # blue keys
        blue_key_rect = self.blue_key_image.get_rect()
        blue_key_rect.topleft = (self.image.get_width() - 946, 100)
        self.image.blit(self.blue_key_image, blue_key_rect)
        blue_key_count = self.key_font.render(str(self.character.blue_keys_collected) + ' / 2', True, (195, 195, 195))
        self.image.blit(blue_key_count,
                        (blue_key_rect.right + 10, blue_key_rect.centery - blue_key_count.get_height() // 2))

