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
    keys_group = pg.sprite.Group()
    chave_amarela = Collectable(700, 620, 'chave_dourada.png', 0.25)
    chave_azul = Collectable(900, 620, 'chave_azul.png', 0.25)
    jaula = Collectable(1000, 604, 'jaula.png', 1)

    keys_group.add(chave_amarela, chave_azul, jaula)

    # criação morangos
    morango1 = Collectable(400, 620, 'morango.png', 0.54)
    morango2 = Collectable(400, 560, 'morango.png', 0.54)
    morango3 = Collectable(450, 560, 'morango.png', 0.54)
    morango4 = Collectable(450, 620, 'morango.png', 0.54)
    morango5 = Collectable(500, 620, 'morango.png', 0.54)
    morango6 = Collectable(500, 560, 'morango.png', 0.54)
    morango7 = Collectable(550, 560, 'morango.png', 0.54)
    morango8 = Collectable(550, 620, 'morango.png', 0.54)
    morango9 = Collectable(200, 560, 'morango.png', 0.54)
    morango10 = Collectable(200, 620, 'morango.png', 0.54)
    morango11 = Collectable(250, 560, 'morango.png', 0.54)
    morango12 = Collectable(250, 620, 'morango.png', 0.54)
    morango13 = Collectable(300, 560, 'morango.png', 0.54)
    morango14 = Collectable(300, 620, 'morango.png', 0.54)
    morango15 = Collectable(350, 560, 'morango.png', 0.54)
    morango16 = Collectable(350, 620, 'morango.png', 0.54)
    keys_group.add(morango1, morango2, morango3, morango4, morango5, morango6, morango7, morango8, morango9, morango10, morango11, morango12, morango13, morango14, morango15, morango16)

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

        keys_group.update(llama)

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

        for key in keys_group:
            key.draw(screen)
        allsprites.update(screen.get_size()[0], screen.get_size()[1], grounds)
        allsprites.draw(screen)

        pg.sprite.Group(hud).update()
        pg.sprite.Group(hud).draw(screen)
        grounds.draw(screen)

        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
