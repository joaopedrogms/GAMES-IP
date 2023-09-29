import os
import pygame as pg
from pygame.locals import *
from hud import *
from character import *
from princess import *
from collectables import *
from platforms import *
from holes import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'media')

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

def load_strawberries():
    strawberry1 = Collectable(250, 350, 'strawberry')
    strawberry2 = Collectable(300, 350, 'strawberry')
    strawberry3 = Collectable(350, 350, 'strawberry')
    strawberry4 = Collectable(400, 350, 'strawberry')
    strawberry5 = Collectable(250, 300, 'strawberry')
    strawberry6 = Collectable(300, 300, 'strawberry')
    strawberry7 = Collectable(350, 300, 'strawberry')
    strawberry8 = Collectable(400, 300, 'strawberry')

    strawberry9 = Collectable(650, 450, 'strawberry')
    strawberry10 = Collectable(700, 450, 'strawberry')
    strawberry11 = Collectable(750, 450, 'strawberry')
    strawberry12 = Collectable(800, 450, 'strawberry')
    strawberry13 = Collectable(650, 400, 'strawberry')
    strawberry14 = Collectable(700, 400, 'strawberry')
    strawberry15 = Collectable(750, 400, 'strawberry')
    strawberry16 = Collectable(800, 400, 'strawberry')

    strawberry17 = Collectable(200, 600, 'strawberry')
    strawberry18 = Collectable(250, 600, 'strawberry')
    strawberry19 = Collectable(300, 600, 'strawberry')
    strawberry20 = Collectable(350, 600, 'strawberry')
    strawberry21 = Collectable(200, 550, 'strawberry')
    strawberry22 = Collectable(250, 550, 'strawberry')
    strawberry23 = Collectable(300, 550, 'strawberry')
    strawberry24 = Collectable(350, 550, 'strawberry')
    strawberry25 = Collectable(200, 500, 'strawberry')
    strawberry26 = Collectable(250, 500, 'strawberry')
    strawberry27 = Collectable(300, 500, 'strawberry')
    strawberry28 = Collectable(350, 500, 'strawberry')

    return strawberry1, strawberry2, strawberry3, strawberry4, strawberry5, strawberry6, strawberry7, strawberry8, strawberry9, strawberry10, strawberry11, strawberry12, strawberry13, strawberry14, strawberry15, strawberry16, strawberry17, strawberry18, strawberry19, strawberry20, strawberry21, strawberry22, strawberry23, strawberry24, strawberry25, strawberry26, strawberry27, strawberry28

def load_keys_and_cage():
    yellow_key_1 = Collectable(670, 150, 'yellow_key')
    yellow_key_2 = Collectable(190, 350, 'yellow_key')

    blue_key_1 = Collectable(900, 600, 'blue_key')
    blue_key_2 = Collectable(310, 210, 'blue_key')

    cage = Collectable(1000, 604, 'cage')

    return yellow_key_1, yellow_key_2, blue_key_1, blue_key_2, cage

def load_platforms():
    #obs: o 10 é a largura da cauda do sprite, o que faz o personagem voar se nao for retirada da colisao
    ground_platform_1 = Platform(0, 687, 590 - 10, 90)
    ground_platform_2 = Platform(780 + 10, 687, 590, 90)

    platform_1 = Platform(600, 500, sprite=1)
    platform_2 = Platform(150, 420, sprite=2)
    platform_3 = Platform(550, 230, sprite=1)

    return ground_platform_1, ground_platform_2, platform_1, platform_2, platform_3

def load_holes():
    hole1 = Hole(590, 630, 190, 140)

    return hole1

def main():
    #inicialização do jogo
    pg.init()
    screen = pg.display.set_mode((1080, 760), pg.SCALED)
    pg.display.set_caption('Llama simulator')
    pg.display.set_icon(load_image('icon.png'))

    # grupos de sprites
    collectables_group = pg.sprite.Group()
    platforms_group = pg.sprite.Group()
    sprites_behind_player = pg.sprite.Group()

    # carragamento da iamgem de fundo, coeltáveis e plataformas
    background = load_image('background.png', scale=1)
    background = pg.transform.scale(background, (screen.get_size()[0], screen.get_size()[1]))

    collectables_group.add(load_keys_and_cage(), load_strawberries())
    platforms_group.add(load_platforms())
    sprites_behind_player.add(load_holes())

    # Inicialização de variáveis
    princess = None
    wait_jump_count = 0
    fullscreen_timer = 0
    llama = Character()
    hud = HUD(llama)
    clock = pg.time.Clock()

    going = True
    while going:
        clock.tick(60)

        #saida do jogo
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                going = False

        #update elementos da tela
        collectables_group.update(llama)
        pg.sprite.Group(hud).update()
        llama.update(screen.get_size()[0], platforms_group)

        #desenho de lementos da tela
        screen.blit(background, (0, 0))
        sprites_behind_player.draw(screen)
        collectables_group.draw(screen)
        pg.sprite.Group(hud).draw(screen)
        pg.sprite.RenderPlain(llama).draw(screen)
        platforms_group.draw(screen)

        # inicialização da princesa e fim da fase
        if llama.cage_collected:
            if princess is not None:
                if wait_jump_count < 90:
                    wait_jump_count += 1
                else:
                    llama.can_jump = True
                    princess.update(platforms_group)
            else:
                princess = Princess(965, 600)
                sprites_behind_player.add(princess)
                llama.looking_right = True

        # tela cheia com um contador
        if pg.key.get_pressed()[pg.K_f]:
            if pg.time.get_ticks() - fullscreen_timer > 300:
                pg.display.toggle_fullscreen()
                fullscreen_timer = pg.time.get_ticks()

        '''for platform in platforms_group:
            pg.draw.rect(screen, (255, 0, 0), platform.rect)'''

        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()