import os
import pygame as pg
from pygame.locals import *

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "media")


def load_image(name, colorkey=None, scale=0.3):
    fullpath = os.path.join(data_dir, 'img')
    fullname = os.path.join(fullpath, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)

    return image


class Character(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image('sprite_llama.png')
        self.rect = load_image('sprite_llama.png').get_rect()
        self.image_upper = self.rect.copy()
        self.looking = True
        self.jump = False
        self.hp = 3
        self.attack = 1
        self.speed = 3
        self.chaves_coletadas = 0
        self.chaves_prateadas_coletadas = 0
        self.jaula_coletada = 0

    def update(self, width, heigth):
        top_value = self.rect[1]
        if top_value == 0:
            self.rect = self.rect.move(
                0, pg.display.get_surface().get_size()[1] - self.rect[3])
            self.image_upper = self.rect.copy()

        self._walk(width)
        self._jump(heigth)

    def _jump(self, height):
        up_pressed = pg.key.get_pressed()[pg.K_UP]
        w_pressed = pg.key.get_pressed()[pg.K_w]
        jump_height = 10
        gravity = 0.3

        if (w_pressed or up_pressed) and not self.jump:
            self.jump = True
            self.jump_height = -jump_height

        if self.jump:
            if self.rect.bottom >= height:
                self.rect.y = (height - 1) - self.rect.height
                self.jump = False
            else:
                self.rect.y += self.jump_height
                self.jump_height += gravity

    def _walk(self, width):
        d_pressed = pg.key.get_pressed()[pg.K_d]
        right_pressed = pg.key.get_pressed()[pg.K_RIGHT]
        left_pressed = pg.key.get_pressed()[pg.K_LEFT]
        a_pressed = pg.key.get_pressed()[pg.K_a]

        if d_pressed or right_pressed:
            self.looking = True
            if self.rect.right < width:
                self.rect = self.rect.move(self.speed, 0)
        elif left_pressed or a_pressed:
            self.looking = False
            if self.rect.left > 0:
                self.rect = self.rect.move(-self.speed, 0)

        if self.jump:
            if self.looking:
                self.image = pg.transform.flip(load_image(
                    'sprite_llama_pulo.png'), True, False)
            else:
                self.image = load_image('sprite_llama_pulo.png')
        else:
            if self.looking:
                self.image = pg.transform.flip(
                    load_image('sprite_llama.png'), True, False)
            else:
                self.image = load_image('sprite_llama.png')


class Key(pg.sprite.Sprite):
    def __init__(self, x, y, scale=0.4):
        pg.sprite.Sprite.__init__(self)
        self.original_image = load_image('key-remove.png', scale=0.3)
        self.image = pg.transform.scale(self.original_image, (int(self.original_image.get_width() * scale), int(self.original_image.get_height() * scale)))  # Aplica a escala à imagem
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.collected = False  # Inicialmente, a chave não foi coletada

    def update(self, character):
        if not self.collected:
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.chaves_coletadas += 1  # Incrementa o contador de chaves coletadas no personagem
    
    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)

class Key_prata(pg.sprite.Sprite):
    def __init__(self, x, y, scale=0.5):
        pg.sprite.Sprite.__init__(self)
        self.original_image = load_image('key.jpg', scale=0.3)
        self.image = pg.transform.scale(self.original_image, (int(self.original_image.get_width(
        ) * scale), int(self.original_image.get_height() * scale)))  # Aplica a escala à imagem
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.collected = False  # Inicialmente, a chave não foi coletada

    def update(self, character):
        if not self.collected:
            if self.rect.colliderect(character.rect):
                self.collected = True
                character.chaves_prateadas_coletadas += 1 # Incrementa o contador de chaves coletadas no personagem
    
    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)

class Jaula(pg.sprite.Sprite):
    def __init__(self, x, y, scale=0.6):
        pg.sprite.Sprite.__init__(self)
        self.original_image = load_image('image-remove.png', scale=0.3)
        self.image = pg.transform.scale(self.original_image, (int(self.original_image.get_width() * scale), int(self.original_image.get_height() * scale)))  # Aplica a escala à imagem
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.collected = False  # Inicialmente, a chave não foi coletada

    def update(self, character):
        if not self.collected:
            if character.chaves_coletadas == 3 and character.chaves_prateadas_coletadas == 3 and self.rect.colliderect(character.rect):
                self.collected = True
                character.jaula_coletada += 1 # Incrementa o contador de chaves coletadas no personagem

    def draw(self, screen):	
        if not self.collected:	
            screen.blit(self.image, self.rect)            
    
class Attack(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image("desenho_gota_pixelized-1.png", scale=0.02)
        self.rect = self.image.get_rect()
        self.is_spit = False
        self.to_move = 100
        self.moved = 0


    def update(self, char_class):
        if char_class.looking:
            if self.rect[1] == 0:
                self.rect = self.rect.move(
                    char_class.rect[0] - self.rect[0] + 75, char_class.rect[1] - self.rect[1] + 10)
        else:
            if self.rect[1] == 0:
                self.rect = self.rect.move(
                    char_class.rect[0] - self.rect[0] - 35, char_class.rect[1] - self.rect[1] + 10)

        if char_class.looking and not self.is_spit:
            self.to_move = 100
        elif not char_class.looking and not self.is_spit:
            self.to_move = -100    

        self._spit()
        self._moveSpit(char_class)

    def _spit(self):
        j_pressed = pg.key.get_pressed()[pg.K_j]
        z_pressed = pg.key.get_pressed()[pg.K_z]

        if j_pressed or z_pressed:
            self.is_spit = True

    def _moveSpit(self, char_class):
        if not self.is_spit:
            if char_class.looking:
                self.rect = self.rect.move(
                    char_class.rect[0] - self.rect[0] + 75, char_class.rect[1] - self.rect[1] + 10)
            else:
                self.rect = self.rect.move(
                    char_class.rect[0] - self.rect[0] - 35, char_class.rect[1] - self.rect[1] + 10)
        if self.is_spit:
            #decide pra qual lado o cuspe vai
            if self.to_move > 0 and self.moved < self.to_move :
                self.rect = self.rect.move(6, 0)
                self.moved = self.moved + 6
            elif self.to_move < 0 and self.moved > self.to_move :
                self.rect = self.rect.move(-6, 0)
                self.moved = self.moved - 6
            #traz o cuspe de volta para perto da llama    
            else:
                self.is_spit = False
                self.moved = 0       

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)


def main():
    pg.init()
    screen = pg.display.set_mode((1080, 760), pg.SCALED)
    pg.display.set_caption("Llama simulator")

    width = screen.get_size()[0]
    height = screen.get_size()[1]

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background = load_image('background.jpeg')
    background = pg.transform.scale(background,(width,height))

    # chave
    keys_group = pg.sprite.Group()
    key1 = Key(600, 620)  # Posição da chave
    key2 = Key(700, 620)
    key3 = Key(800, 620)
    imagem_chave = Key(915, 30)
    keys_group.add(key1, key2, key3, imagem_chave)

    # chave prateada
    keys_group_prateada = pg.sprite.Group()
    Key_prateada = Key_prata(300, 620)  #Posição da chave
    Key_prateada2 = Key_prata(400, 620)
    Key_prateada3 = Key_prata(500, 620)
    imagem_chave_prateada = Key_prata(910, 70)
    keys_group_prateada.add(Key_prateada, Key_prateada2, Key_prateada3, imagem_chave_prateada)

    # jaula
    jaula_group = pg.sprite.Group()
    jaula = Jaula(940, 650)  # Posição da jaula
    imagem_jaula = Jaula(920, 130)
    jaula_group.add(jaula, imagem_jaula)

    screen.blit(background, (0, 0))

    print(pg.display.get_surface().get_size())
    pg.display.flip()

    pocoyo = Character()

    allsprites = pg.sprite.RenderPlain((pocoyo))

    pocoyo_attack = Attack()
    attack_sprite = pg.sprite.RenderPlain((pocoyo_attack))

    clock = pg.time.Clock()

    going = True
    while going:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            going = False
        elif going:
            pocoyo.update(screen.get_size()[0], screen.get_size()[1])

        allsprites.update(screen.get_size()[0], screen.get_size()[1])

        keys_group.update(pocoyo)
        keys_group.draw(screen)

        keys_group_prateada.update(pocoyo)
        keys_group_prateada.draw(screen)

        jaula_group.update(pocoyo)
        jaula_group.draw(screen)

        screen.blit(background, (0, 0))
        for key in keys_group:
            key.draw(screen)

        for key_prat in keys_group_prateada:
            key_prat.draw(screen)

        for jaula_imagem in jaula_group:
            jaula_imagem.draw(screen)

        allsprites.draw(screen)

        pocoyo_attack.update(pocoyo)
        if pocoyo_attack.is_spit:
            attack_sprite.draw(screen)

        # Exibe a quantidade de chaves coletadas no canto superior direito da tela
        mensagem = f'{pocoyo.chaves_coletadas}/3'
        mensagem2 = f"{pocoyo.chaves_prateadas_coletadas}/3"
        fonte = pg.font.SysFont('Fixedsys', 40)
        texto_formatado = fonte.render(mensagem, True, (255, 255, 50))
        texto_formatado2 = fonte.render(mensagem2, True, (150, 150, 150))
        # Define a posição da frase no canto superior direito
        screen.blit(texto_formatado, (950, 15))
        screen.blit(texto_formatado2, (950, 55))

        # Exibe a quantidade de jaulas coletadas no canto superior direito da tela
        mensagem_jaula = f'{pocoyo.jaula_coletada}/1'
        texto_jaula = fonte.render(mensagem_jaula, True, (255, 255, 50))
        screen.blit(texto_jaula, (950, 110))
        
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
