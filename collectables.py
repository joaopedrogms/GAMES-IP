import pygame as pg

class Collectable(pg.sprite.Sprite):
    def __init__(self, x, y, imagem, scale):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.figura = imagem
        self.scale = scale
        self.original_image = load_image(self.figura)
        self.image = pg.transform.scale(self.original_image, (int(self.original_image.get_width() * scale), int(self.original_image.get_height() * scale)))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
        self.collected = False

    def update(self, character):
        if not self.collected and self.figura == 'chave_dourada.png':
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.chaves_coletadas += 1

        if not self.collected and self.figura == 'chave_azul.png':
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.chaves_azuis_coletadas += 1

        if not self.collected and self.figura == 'morango.png':
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.morangos_coletados += 1

        if not self.collected:
            if character.chaves_coletadas == 1 and character.chaves_azuis_coletadas == 1 and self.rect.colliderect(
                    character.rect):
                self.collected = True
                character.jaula_coletada = True

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)

