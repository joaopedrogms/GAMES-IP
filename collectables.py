import pygame as pg

quantity_golden_keys = 0
quantity_silver_keys = 0

class Collectable(pg.sprite.Sprite):
    def __init__(self, x, y, object):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.object = object
        if self.object == 'strawberry':
            self.image = load_image('strawberry.png', scale=0.149)
        elif self.object == 'golden_key':
            self.image = load_image('golden_key.png', scale=0.05)
            global quantity_golden_keys
            quantity_golden_keys += 1
        elif self.object == 'silver_key':
            self.image = load_image('silver_key.png', scale=0.05)
            global quantity_silver_keys
            quantity_silver_keys += 1
        elif self.object == 'cage':
            self.image = load_image('cage.png', scale=0.3)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.collected = False

    def update(self, character):
        if not self.collected and self.rect.colliderect(character.rect):
            if self.object == 'cage':
                if character.golden_keys_collected >= quantity_golden_keys and character.silver_keys_collected >= quantity_silver_keys:
                    self.collected = True
                    character.cage_collected = True
                    self.kill()
            else:
                if self.object == 'golden_key':
                    character.golden_keys_collected += 1
                elif self.object == 'silver_key':
                    character.silver_keys_collected += 1
                elif self.object == 'strawberry':
                    character.strawberries_collected += 1

                self.kill()

    @classmethod
    def reset_collectable_keys(cls):
        global quantity_golden_keys
        global quantity_silver_keys
        quantity_golden_keys = 0
        quantity_silver_keys = 0

    @classmethod
    def get_quantity_golden_keys(cls):
        return quantity_golden_keys

    @classmethod
    def get_quantity_silver_keys(cls):
        return quantity_golden_keys