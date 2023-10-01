import pygame as pg
from collectables import *

class HUD(pg.sprite.Sprite):
    def __init__(self, character, mapa):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.character = character
        self.heart_image = load_image('heart.png', scale=0.05)
        self.golden_key_image = load_image('golden_key.png', scale=0.05)
        self.silver_key_image = load_image('silver_key.png', scale=0.05)
        self.strawberry_image = load_image('strawberry.png', scale=0.149)
        self.map_text = f'Mapa: {mapa}'
        self.rect = self.heart_image.get_rect()
        self.rect.topleft = (10, 10)
        try:
            self.game_font = pg.font.Font('media/font/daydream.ttf', 15)
            self.map_font = pg.font.Font('media/font/daydream.ttf', 30)
        except:
            self.game_font = pg.font.Font(None, 30)
            self.map_font = pg.font.Font(None, 45)

    def update(self):
        self.image = pg.Surface((1900, 1900), pg.SRCALPHA)

        # hearts
        heart_x = 10
        for _ in range(self.character.hp):
            self.image.blit(self.heart_image, (heart_x, 10))
            heart_x += 35

        # strawberries
        strawberry_rect = self.strawberry_image.get_rect()
        strawberry_rect.topleft = (954, 10)
        self.image.blit(self.strawberry_image, strawberry_rect)
        strawberry_count = self.game_font.render(str(self.character.strawberries_collected), True, (196, 0, 40))
        self.image.blit(strawberry_count, (1001, 23))

        # yellow keys
        golden_key_rect = self.golden_key_image.get_rect()
        golden_key_rect.topleft = (954, 56)
        self.image.blit(self.golden_key_image, golden_key_rect)
        golden_key_count = self.game_font.render(str(self.character.golden_keys_collected) + ' / ' + str(Collectable.get_quantity_golden_keys()), True, (255, 255, 160))
        self.image.blit(golden_key_count, (1004, 66))

        # silver keys
        silver_key_rect = self.silver_key_image.get_rect()
        silver_key_rect.topleft = (954, 100)
        self.image.blit(self.silver_key_image, silver_key_rect)
        silver_key_count = self.game_font.render(str(self.character.silver_keys_collected) + ' / ' + str(Collectable.get_quantity_silver_keys()), True, (195, 195, 195))
        self.image.blit(silver_key_count, (1004, 110))

        # map text
        self.image.blit(self.game_font.render(self.map_text, True, (255, 255, 255)), (494, 10))