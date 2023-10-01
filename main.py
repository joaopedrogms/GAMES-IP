import sys
import os
import pygame as pg

from hud import *
from character import *
from princess import *
from load import *

def load_image(name, scale=0.3):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'media')
    fullpath = os.path.join(data_dir, 'img')
    fullname = os.path.join(fullpath, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    return image

def menu():
    pg.init()
    screen = pg.display.set_mode((1080, 760), pg.SCALED)
    pg.display.set_caption('Llama Adventures')
    pg.display.set_icon(load_image('icon.png', scale=1))
    background = load_image('menu.png', scale=1)

    title_button = load_image('llama_adventures.png', scale=1.09)
    title_button_rect = title_button.get_rect(center=(screen.get_width() // 2, 250))
    play_button = load_image('menu_play.png', scale=1)
    play_button_rect = play_button.get_rect(center=(screen.get_width() // 2, 530))

    cloud_group = pg.sprite.Group()
    cloud_group.add(load_clouds_menu())
    clock = pg.time.Clock()
    fullscreen_timer = 0

    going = True
    while going:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                sys.exit()
            elif event.type == pg.MOUSEMOTION:
                if play_button_rect.collidepoint(event.pos):
                    play_button = load_image('mouse_on_menu_play.png', scale=1)
                else:
                    play_button = load_image('menu_play.png', scale=1)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    main(screen, mapa=1)
                    going = False

        if pg.key.get_pressed()[pg.K_f]:
            if pg.time.get_ticks() - fullscreen_timer > 300:
                pg.display.toggle_fullscreen()
                fullscreen_timer = pg.time.get_ticks()

        #background
        screen.blit(background, (0, 0))

        #desenho das nuvens
        cloud_group.update()
        cloud_group.draw(screen)

        #desenho do titulo e botao:
        screen.blit(title_button, title_button_rect.topleft)
        screen.blit(play_button, play_button_rect.topleft)

        pg.display.flip()

    pg.quit()

def main(screen, llama=None, mapa=1):

    # carragamento da iamgem de fundo, coeltáveis e plataformas
    background = load_image('background.png', scale=1)
    background = pg.transform.scale(background, (screen.get_size()[0], screen.get_size()[1]))

    # grupos de sprites
    collectables_group = pg.sprite.Group()
    platforms_group = pg.sprite.Group()
    sprites_behind_player = pg.sprite.Group()

    if mapa == 1:
        princess_x = 965
        princess_y = 600
        collectables_group.add(load_keys_and_cage_1(), load_strawberries_1())
        platforms_group.add(load_platforms_1())
    elif mapa == 2:
        princess_x = 965
        princess_y = 600
        collectables_group.add(load_keys_and_cage_2(), load_strawberries_2())
        platforms_group.add(load_platforms_2())
        sprites_behind_player.add(load_holes_2())
    elif mapa == 3:
        princess_x = 965
        princess_y = 600
        collectables_group.add(load_keys_and_cage_3(), load_strawberries_3())
        platforms_group.add(load_platforms_3())
        sprites_behind_player.add(load_holes_3())
    elif mapa == 4:
        princess_x = 965
        princess_y = 600
        collectables_group.add(load_keys_and_cage_4(), load_strawberries_4())
        platforms_group.add(load_platforms_4())
        sprites_behind_player.add(load_holes_4())
    elif mapa == 5:
        princess_x = 965
        princess_y = 600
        collectables_group.add(load_keys_and_cage_5(), load_strawberries_5())
        platforms_group.add(load_platforms_5())
        sprites_behind_player.add(load_holes_5())

    # Inicialização de variáveis
    fullscreen_timer = 0
    wait_jump_count = 0
    princess = None

    if mapa == 1:
        llama = Character()
    else:
        llama.cage_collected = False

    hud = HUD(llama, mapa)

    clock = pg.time.Clock()

    going = True
    while going:
        clock.tick(60)

        #saida do jogo
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
                sys.exit()

        #update elementos da tela
        collectables_group.update(llama)
        pg.sprite.Group(hud).update()
        llama.update(screen.get_size()[0], platforms_group)

        #desenho de lementos da tela
        screen.blit(background, (0, 0))
        sprites_behind_player.draw(screen)
        collectables_group.draw(screen)
        pg.sprite.RenderPlain(llama).draw(screen)
        pg.sprite.Group(hud).draw(screen)
        platforms_group.draw(screen)

        # inicialização da princesa e fim da fase
        if llama.cage_collected:
            if princess is not None:
                if wait_jump_count < 90:
                    wait_jump_count += 1
                else:
                    llama.can_jump = True
                    princess.update(platforms_group)
                    if princess.jump_count > 3 and princess.vertical_speed > 0:
                        #reinicialização do persoangem princiapal:
                        Collectable.reset_collectable_keys()
                        llama.golden_keys_collected = 0
                        llama.silver_keys_collected = 0
                        llama.rect.bottomleft = (0, 687)
                        llama.cage_collected = False
                        llama.can_jump = False

                        #inicialização do proximo mapa
                        mapa += 1
                        main(screen, llama, mapa)
                        going = False
            else:
                princess = Princess(princess_x, princess_y)

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
    menu()