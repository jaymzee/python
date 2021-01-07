# benchmark how long to fill screen pixel by pixel

import sys
import pygame as pg
import math

SIZE = (1000, 1000)
WIDTH, HEIGHT = SIZE

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

colors = [BLACK, GREEN]


def draw(surf, n):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            surf.set_at((x, y), colors[n & 1]);


def main():
    pg.init()
    surf = pg.display.set_mode(SIZE)
    pg.display.set_caption('fill')
    for n in range(10):
        draw(surf, n)
        pg.display.flip()


if __name__ == '__main__':
    main()
