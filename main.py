import pygame as pg
import sys

RESOLUTION = {
    '540': (960, 540),
    '576': (1024, 576),
    '720': (1280, 720),
    '768': (1366, 768),
    '999': (1776, 999),
    '1080': (1920,1080),
    '1440': (2560, 1440)
}
FPS = 60
TITLE = 'My Game'

pg.init()

screen = pg.display.set_mode(RESOLUTION['999'])
screct = screen.get_rect()

# pg.display.set_icon()
pg.display.set_caption(TITLE)

clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

while True:
    dt = clock.tick(FPS)/1000

    screen.fill(pg.Color('black'))
    all_sprites.update(dt)
    all_sprites.draw(screen)
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
