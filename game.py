import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "media")


def load_image(name, colorkey=None, scale=1):
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

    return image, image.get_rect()


class Character(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('sprite_llama.png')
        self.image_upper = self.rect.copy()
        self.looking = True
        self.jump = False
        self.hp = 3
        self.attack = 1
        self.speed = 3

    def update(self, width, heigth, screen):
        top_value = self.rect[1]
        if top_value == 0:
            self.rect = self.rect.move(
                0, pg.display.get_surface().get_size()[1] - self.rect[3])
            self.image_upper = self.rect.copy()

        self._walk(width)
        self._jump(heigth)
        self._spit(screen)

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

    def _spit(self, screen):
        j_pressed = pg.key.get_pressed()[pg.K_j]
        z_pressed = pg.key.get_pressed()[pg.K_z]

        angle = 0
        if j_pressed or z_pressed:
            image_spit = load_image("desenho_gota_pixelized-1.png.png")
            image_rect = image_spit.get_rect()
            screen.blit(image_spit, (self.rect[0] + 10, self.rect[1] + 10))

            if angle == 60:
                angle_changer = -1
            elif angle == -60:
                angle_changer = 1

            center_x = image_rect[0]
            center_y = image_rect[1]
            radius = 50
            line_vector = pg.math.Vector2(1, 0)
            angle_changer = 1

            angle += angle_changer
            rot_vector = line_vector.rotate(angle) * radius
            start_line = round(center_x + rot_vector.x), round(center_y + rot_vector.y)
            end_line = round(center_x - rot_vector.x), round(center_y - rot_vector.y)

            pg.draw.line(screen, (0, 0, 0), start_line, end_line, 4)  



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
                self.image = pg.transform.flip(load_image('sprite_llama_pulo.png'), True, False)
            else:
                self.image = load_image('sprite_llama_pulo.png')
        else:
            if self.looking:
                self.image = pg.transform.flip(load_image('sprite_llama.png'), True, False)
            else:
                self.image = load_image('sprite_llama.png')     

def main():

    pg.init()
    screen = pg.display.set_mode((1080, 760), pg.SCALED)
    pg.display.set_caption("Llama simulator")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((128, 128, 128))

    screen.blit(background, (0, 0))
    print(pg.display.get_surface().get_size())
    pg.display.flip()

    pocoyo = Character()
    allsprites = pg.sprite.RenderPlain((pocoyo))
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
            pocoyo.update(screen.get_size()[0], screen.get_size()[1], screen)

        allsprites.update(screen.get_size()[0], screen.get_size()[1])

        keys_group.update(pocoyo)
        keys_group.draw(screen)

        screen.blit(background, (0, 0))
        allsprites.draw(screen)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
