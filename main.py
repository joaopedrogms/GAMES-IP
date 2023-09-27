import os
import pygame as pg
from pygame.locals import *
from hud import *
from character import *
from princess import *
from collectables import *
from plataforms import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'media')

blue_keys = 10

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

def main():
    global sprites_behind_player
    sprites_behind_player = pg.sprite.Group()

    pg.init()
    screen = pg.display.set_mode((1080, 760), pg.SCALED)
    pg.display.set_caption('Llama simulator')
    icon = pg.image.load('icon.png')
    pg.display.set_icon(icon)

    width = screen.get_size()[0]
    height = screen.get_size()[1]

    background = pg.Surface(screen.get_size())
    background = load_image('background.png', scale=1)
    background = pg.transform.scale(background, (width, height))
    colllectables_group = pg.sprite.Group()
    chave_amarela = Collectable(700, 620, 'yellow_key')
    chave_azul = Collectable(900, 620, 'blue_key')
    jaula = Collectable(1000, 604, 'cage')

    colllectables_group.add(chave_amarela, chave_azul, jaula)

    # criação morangos
    morango1 = Collectable(400, 620, 'strawberry')
    morango2 = Collectable(400, 560, 'strawberry')
    morango3 = Collectable(450, 560, 'strawberry')
    morango4 = Collectable(450, 620, 'strawberry')
    morango5 = Collectable(500, 620, 'strawberry')
    morango6 = Collectable(500, 560, 'strawberry')
    morango7 = Collectable(550, 560, 'strawberry')
    morango8 = Collectable(550, 620, 'strawberry')
    morango9 = Collectable(200, 560, 'strawberry')
    morango10 = Collectable(200, 620, 'strawberry')
    morango11 = Collectable(250, 560, 'strawberry')
    morango12 = Collectable(250, 620, 'strawberry')
    morango13 = Collectable(300, 560, 'strawberry')
    morango14 = Collectable(300, 620, 'strawberry')
    morango15 = Collectable(350, 560, 'strawberry')
    morango16 = Collectable(350, 620, 'strawberry')
    colllectables_group.add(morango1, morango2, morango3, morango4, morango5, morango6, morango7, morango8, morango9, morango10, morango11, morango12, morango13, morango14, morango15, morango16)

    # criação do chão
    grounds = pg.sprite.Group()
    ground = Plataform(0, 687, 1080, 70)
    plataforma1 = Plataform(500, 400, 50, 50)
    grounds.add(ground)

    screen.blit(background, (0, 0))
    print(pg.display.get_surface().get_size())
    pg.display.flip()

    princess = None
    contador_pulo = 0
    llama = Character()

    global allsprites
    allsprites = pg.sprite.RenderPlain(llama)
    clock = pg.time.Clock()

    hud = HUD(llama)

    going = True
    while going:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            going = False
        elif going:
            llama.update(screen.get_size()[0], screen.get_size()[1], grounds)

        colllectables_group.update(llama)

        screen.blit(background, (0, 0))

        sprites_behind_player.draw(screen)

        if llama.jaula_coletada:
            if princess != None:
                if contador_pulo < 90:
                    contador_pulo += 1
                else:
                    princess._jump(screen.get_size()[1], grounds)
            else:
                princess = Princess(965, 600)
                sprites_behind_player.add(princess)

        for collectable in colllectables_group:
            collectable.draw(screen)

        allsprites.update(screen.get_size()[0], screen.get_size()[1], grounds)
        allsprites.draw(screen)

        pg.sprite.Group(hud).update()
        pg.sprite.Group(hud).draw(screen)
        grounds.draw(screen)

        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
