import os
import pygame as pg
from pygame.locals import *
from hud import *
from character import *
from princess import *
from collectables import *
from platforms import *

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
    strawberry1 = Collectable(400, 620, 'strawberry')
    strawberry2 = Collectable(400, 560, 'strawberry')
    strawberry3 = Collectable(450, 560, 'strawberry')
    strawberry4 = Collectable(450, 620, 'strawberry')
    strawberry5 = Collectable(500, 620, 'strawberry')
    strawberry6 = Collectable(500, 560, 'strawberry')
    strawberry7 = Collectable(150, 560, 'strawberry')
    strawberry8 = Collectable(150, 620, 'strawberry')

    strawberry9 = Collectable(200, 560, 'strawberry')
    strawberry10 = Collectable(200, 620, 'strawberry')
    strawberry11 = Collectable(250, 560, 'strawberry')
    strawberry12 = Collectable(250, 620, 'strawberry')
    strawberry13 = Collectable(300, 560, 'strawberry')
    strawberry14 = Collectable(300, 620, 'strawberry')
    strawberry15 = Collectable(350, 560, 'strawberry')
    strawberry16 = Collectable(350, 620, 'strawberry')

    strawberry17 = Collectable(200, 500, 'strawberry')
    strawberry18 = Collectable(250, 500, 'strawberry')
    strawberry19 = Collectable(300, 500, 'strawberry')
    strawberry20 = Collectable(350, 500, 'strawberry')
    strawberry21 = Collectable(400, 500, 'strawberry')
    strawberry22 = Collectable(450, 500, 'strawberry')
    strawberry23 = Collectable(500, 500, 'strawberry')
    strawberry24 = Collectable(150, 500, 'strawberry')

    return strawberry1, strawberry2, strawberry3, strawberry4, strawberry5, strawberry6, strawberry7, strawberry8, strawberry9, strawberry10, strawberry11, strawberry12, strawberry13, strawberry14, strawberry15, strawberry16, strawberry17, strawberry18, strawberry19, strawberry20, strawberry21, strawberry22, strawberry23, strawberry24

def load_keys_and_cage():
    yellow_key_1 = Collectable(700, 620, 'yellow_key')
    yellow_key_2 = Collectable(600, 500, 'yellow_key')

    blue_key_1 = Collectable(900, 620, 'blue_key')
    blue_key_2 = Collectable(700, 500, 'blue_key')

    cage = Collectable(1000, 604, 'cage')

    return yellow_key_1, yellow_key_2, blue_key_1, blue_key_2, cage

def load_platforms():
    ground_plataform = Platform(0, 687, 1080, 70)
    plataform = Platform(600, 400, 100, 10)

    return ground_plataform, plataform

def main():
    global sprites_behind_player
    sprites_behind_player = pg.sprite.Group()

    pg.init()
    screen = pg.display.set_mode((1080, 760), pg.SCALED)
    pg.display.set_caption('Llama simulator')
    pg.display.set_icon(load_image('icon.png'))

    # groups
    colllectables_group = pg.sprite.Group()
    platforms_group = pg.sprite.Group()

    background = load_image('background.png', scale=1)
    background = pg.transform.scale(background, (screen.get_size()[0], screen.get_size()[1]))

    colllectables_group.add(load_keys_and_cage(), load_strawberries())
    platforms_group.add(load_platforms())

    screen.blit(background, (0, 0))
    print(pg.display.get_surface().get_size())
    pg.display.flip()

    princess = None
    wait_jump_count = 0
    llama = Character()

    global allsprites
    allsprites = pg.sprite.RenderPlain(llama)
    clock = pg.time.Clock()

    hud = HUD(llama)

    fullscreen_timer = 0

    going = True
    while going:
        clock.tick(60)

        #checagem de fechamento do jogo
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            going = False

        colllectables_group.update(llama)

        screen.blit(background, (0, 0))

        sprites_behind_player.draw(screen)

        #spawn da princesa lhama e final da fase
        if llama.cage_collected:
            if princess != None:
                if wait_jump_count < 90:
                    wait_jump_count += 1
                else:
                    llama.can_jump = True
                    princess.update(platforms_group)
            else:
                princess = Princess(965, 600)
                sprites_behind_player.add(princess)

        for collectable in colllectables_group:
            collectable.draw(screen)

        #mudar o jogo para tela cheia, com um contador
        if pg.key.get_pressed()[pg.K_f]:
            if pg.time.get_ticks() - fullscreen_timer > 300:
                pg.display.toggle_fullscreen()
                fullscreen_timer = pg.time.get_ticks()

        pg.sprite.Group(hud).update()
        pg.sprite.Group(hud).draw(screen)

        allsprites.draw(screen)
        platforms_group.draw(screen)
        allsprites.update(screen.get_size()[0], platforms_group)

        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()