import pygame as pg

quantity_yellow_keys = 0
quantity_blue_keys = 0

class Collectable(pg.sprite.Sprite):
    def __init__(self, x, y, object):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.object = object
        if self.object == 'strawberry':
            self.image = load_image('strawberry.png', scale=0.16)
        elif self.object == 'yellow_key':
            self.image = load_image('yellow_key.png', scale=0.065)
            global quantity_yellow_keys
            quantity_yellow_keys += 1
        elif self.object == 'blue_key':
            self.image = load_image('blue_key.png', scale=0.065)
            global quantity_blue_keys
            quantity_blue_keys += 1
        elif self.object == 'cage':
            self.image = load_image('cage.png', scale=0.3)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.collected = False

    def update(self, character):
        if not self.collected and self.object == 'yellow_key':
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.yellow_keys_collected += 1

        if not self.collected and self.object == 'blue_key':
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.blue_keys_collected += 1

        if not self.collected and self.object == 'strawberry':
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.strawberries_collected += 1

        if not self.collected and self.object == 'cage':
            if character.yellow_keys_collected == quantity_yellow_keys and character.blue_keys_collected == quantity_blue_keys and self.rect.colliderect(character.rect):
                self.collected = True
                character.cage_collected = True

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)