import pygame as pg

class HUD(pg.sprite.Sprite):
    def __init__(self, character):
        from main import load_image
        pg.sprite.Sprite.__init__(self)
        self.character = character
        self.heart_image = load_image('coracao.png', scale=0.06)
        self.chave_dourada_image = load_image('chave_dourada.png', scale=0.065)
        self.chave_azul_image = load_image('chave_azul.png', scale=0.065)
        self.morango_image = load_image('morango.png', scale=0.16)
        self.rect = self.heart_image.get_rect()
        self.rect.topleft = (10, 10)
        self.key_font = pg.font.Font('daydream.ttf', 15)

    def update(self):
        self.image = pg.Surface((1900, 1900), pg.SRCALPHA)
        self.image.fill((0, 0, 0, 0))

        # corações
        heart_x = 10
        for _ in range(self.character.hp):
            self.image.blit(self.heart_image, (heart_x, 10))
            heart_x += 40

        # morangos
        morango_rect = self.morango_image.get_rect()
        morango_rect.topleft = (self.image.get_width() - 920, 10)
        self.image.blit(self.morango_image, morango_rect)
        morango_count = self.key_font.render(str(self.character.morangos_coletados + (self.character.vidas_adicionadas * 10)), True, (255, 0, 0))
        self.image.blit(morango_count, (morango_rect.right + 10, morango_rect.centery))

        # chaves amarelas
        chave_dourada_rect = self.chave_dourada_image.get_rect()
        chave_dourada_rect.topleft = (self.image.get_width() - 930, 50)
        self.image.blit(self.chave_dourada_image, chave_dourada_rect)
        chave_dourada_count = self.key_font.render(str(self.character.chaves_coletadas), True, (255, 255, 50))
        self.image.blit(chave_dourada_count, (
        chave_dourada_rect.right + 10, chave_dourada_rect.centery - chave_dourada_count.get_height() // 2))

        # chaves azuis
        chave_azul_rect = self.chave_azul_image.get_rect()
        chave_azul_rect.topleft = (self.image.get_width() - 930, 90)
        self.image.blit(self.chave_azul_image, chave_azul_rect)
        chave_azul_count = self.key_font.render(str(self.character.chaves_azuis_coletadas), True, (60, 135, 210))
        self.image.blit(chave_azul_count,
                        (chave_azul_rect.right + 10, chave_azul_rect.centery - chave_azul_count.get_height() // 2))

