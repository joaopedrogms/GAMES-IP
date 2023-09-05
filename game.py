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

    image = image.convert()
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
        self.jump_call_counter = 1
        self.hp = 3
        self.attack = 1
        self.speed = 10

    def update(self, width, heigth):
        # responsável por decidir o que o personagem vai fazer
        top_value = self.rect[1]
        if top_value == 0:
            self.rect = self.rect.move(
                0, pg.display.get_surface().get_size()[1] - self.rect[3])
            self.image_upper = self.rect.copy()

        self._walk(width)
        self._jump(heigth)
        # if seçf

    def _jump(self, heigth):
        if (pg.key.get_pressed()[pg.K_w]) or (pg.key.get_pressed()[pg.K_UP]):
            # print(self.rect)
            if self.rect[1] >= self.image_upper[1] - 50:
                # print(self.image_upper)
                print(self.rect)
                self.rect = self.rect.move(0, -5)
        else:
            if self.rect[1] != self.image_upper[1]:
                if self.jump_call_counter == 5:
                    self.jump_call_counter = 0
                elif self.jump_call_counter < 5 and self.rect.bottom < heigth:
                    self.rect = self.rect.move(0, 5)
                    self.jump_call_counter = self.jump_call_counter + 1

    def _walk(self, width):
        if (pg.key.get_pressed()[pg.K_d]) or (pg.key.get_pressed()[pg.K_RIGHT]):
            if self.rect.right < width:
                self.rect = self.rect.move(self.speed, 0)
        if (pg.key.get_pressed()[pg.K_a]) or (pg.key.get_pressed()[pg.K_LEFT]):
            if self.rect.left > 0:
                self.rect = self.rect.move(-self.speed, 0)


def main():

    pg.init()
    screen = pg.display.set_mode((640, 480), pg.SCALED)
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
            pocoyo.update(screen.get_size()[0], screen.get_size()[1])

        allsprites.update(screen.get_size()[0], screen.get_size()[1])

        screen.blit(background, (0, 0))
        allsprites.draw(screen)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
