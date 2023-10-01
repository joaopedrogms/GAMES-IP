from collectables import *
from platforms import *
from holes import *
from clouds import *
def load_clouds_menu():
    cloud_1 = Cloud(-700, 60, 'sprite_platform_1.png')
    cloud_2 = Cloud(1300, 530, 'sprite_platform_2.png')
    cloud_3 = Cloud(180, 380, 'sprite_platform_3.png')

    return cloud_1, cloud_2, cloud_3
def load_platforms_1():
    #obs: o 10 é a largura da cauda do sprite, o que faz o personagem voar se nao for retirada da colisao
    ground_platform_1 = Platform(0, 687, 1080, 90)

    platform_1 = Platform(365, 500, sprite=3)

    return ground_platform_1, platform_1
def load_holes_1():
    #hole1 = Hole(510, 630, 270, 140)

    return None
def load_strawberries_1():
    strawberry1 = Collectable(350, 630, 'strawberry')
    strawberry2 = Collectable(400, 630, 'strawberry')
    strawberry3 = Collectable(450, 630, 'strawberry')
    strawberry4 = Collectable(500, 630, 'strawberry')
    strawberry5 = Collectable(550, 630, 'strawberry')
    strawberry6 = Collectable(600, 630, 'strawberry')
    strawberry7 = Collectable(650, 630, 'strawberry')
    strawberry8 = Collectable(700, 630, 'strawberry')

    strawberry9 = Collectable(350, 580, 'strawberry')
    strawberry10 = Collectable(400, 580, 'strawberry')
    strawberry11 = Collectable(450, 580, 'strawberry')
    strawberry12 = Collectable(500, 580, 'strawberry')
    strawberry13 = Collectable(550, 580, 'strawberry')
    strawberry14 = Collectable(600, 580, 'strawberry')
    strawberry15 = Collectable(650, 580, 'strawberry')
    strawberry16 = Collectable(700, 580, 'strawberry')


    return strawberry1, strawberry2, strawberry3, strawberry4, strawberry5, strawberry6, strawberry7, strawberry8,\
        strawberry9, strawberry10, strawberry11, strawberry12, strawberry13, strawberry14, strawberry15, strawberry16

def load_keys_and_cage_1():
    golden_key_1 = Collectable(600, 430, 'golden_key')

    silver_key_1 = Collectable(430, 430, 'silver_key')

    cage = Collectable(1000, 604, 'cage')

    return golden_key_1, silver_key_1, cage

def load_platforms_4():
    #obs: o 10 é a largura da cauda do sprite, o que faz o personagem voar se nao for retirada da colisao
    ground_platform_1 = Platform(0, 687, 510 - 10, 90)
    ground_platform_2 = Platform(780 + 10, 687, 590, 90)

    platform_1 = Platform(600, 500, sprite=1)
    platform_2 = Platform(140, 410, sprite=2)
    platform_3 = Platform(400, 220, sprite=3)

    return ground_platform_1, ground_platform_2, platform_1, platform_2, platform_3
def load_holes_4():
    hole1 = Hole(510, 630, 270, 140)

    return hole1
def load_strawberries_4():
    strawberry1 = Collectable(250, 370, 'strawberry')
    strawberry2 = Collectable(300, 370, 'strawberry')
    strawberry3 = Collectable(350, 370, 'strawberry')
    strawberry4 = Collectable(400, 370, 'strawberry')
    strawberry5 = Collectable(250, 320, 'strawberry')
    strawberry6 = Collectable(300, 320, 'strawberry')
    strawberry7 = Collectable(350, 320, 'strawberry')
    strawberry8 = Collectable(400, 320, 'strawberry')

    strawberry9 = Collectable(650, 450, 'strawberry')
    strawberry10 = Collectable(700, 450, 'strawberry')
    strawberry11 = Collectable(750, 450, 'strawberry')
    strawberry12 = Collectable(800, 450, 'strawberry')
    strawberry13 = Collectable(650, 400, 'strawberry')
    strawberry14 = Collectable(700, 400, 'strawberry')
    strawberry15 = Collectable(750, 400, 'strawberry')
    strawberry16 = Collectable(800, 400, 'strawberry')

    strawberry17 = Collectable(200, 630, 'strawberry')
    strawberry18 = Collectable(250, 630, 'strawberry')
    strawberry19 = Collectable(300, 630, 'strawberry')
    strawberry20 = Collectable(350, 630, 'strawberry')
    strawberry21 = Collectable(200, 580, 'strawberry')
    strawberry22 = Collectable(250, 580, 'strawberry')
    strawberry23 = Collectable(300, 580, 'strawberry')
    strawberry24 = Collectable(350, 580, 'strawberry')
    strawberry25 = Collectable(200, 530, 'strawberry')
    strawberry26 = Collectable(250, 530, 'strawberry')
    strawberry27 = Collectable(300, 530, 'strawberry')
    strawberry28 = Collectable(350, 530, 'strawberry')

    strawberry29 = Collectable(550, 180, 'strawberry')
    strawberry30 = Collectable(600, 180, 'strawberry')
    strawberry31 = Collectable(550, 130, 'strawberry')
    strawberry32 = Collectable(600, 130, 'strawberry')
    strawberry33 = Collectable(650, 180, 'strawberry')
    strawberry34 = Collectable(650, 130, 'strawberry')

    strawberry35 = Collectable(40, 500, 'strawberry')


    return strawberry1, strawberry2, strawberry3, strawberry4, strawberry5, strawberry6, strawberry7, strawberry8,\
        strawberry9, strawberry10, strawberry11, strawberry12, strawberry13, strawberry14, strawberry15, strawberry16,\
        strawberry17, strawberry18, strawberry19, strawberry20, strawberry21, strawberry22, strawberry23, strawberry24,\
        strawberry25, strawberry26, strawberry27, strawberry28, strawberry29, strawberry30, strawberry31, strawberry32, \
        strawberry33, strawberry34, strawberry35
def load_keys_and_cage_4():
    golden_key_1 = Collectable(900, 600, 'golden_key')
    golden_key_2 = Collectable(310, 210, 'golden_key')

    silver_key_1 = Collectable(450, 150, 'silver_key')
    silver_key_2 = Collectable(190, 350, 'silver_key')

    cage = Collectable(1000, 604, 'cage')

    return golden_key_1, golden_key_2, silver_key_1, silver_key_2, cage