import sys
import pygame as pg
import math
from math import pi

SIZE = (1000, 1000)
WIDTH, HEIGHT = SIZE
CX = WIDTH / 2
CY = HEIGHT / 2
R = 450
FPS = 500
POINTS = 500


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)


def draw(surf, font, fps, factor):
    surf.fill(BLACK)
    fps_text = font.render("%d fps" % fps, 0, YELLOW)
    fac_text = font.render("%.3f" % factor, 0, WHITE)
    surf.blit(fps_text, (10,10))
    surf.blit(fac_text, (int(CX - R), int(CY / 4)))
    for n in range(POINTS):
        n2 = factor * n
        theta = 2 * pi * n / POINTS
        phi = 2 * pi * n2 / POINTS
        x = R * math.cos(theta)
        y = R * math.sin(theta)
        x2 = R * math.cos(phi)
        y2 = R * math.sin(phi)
        pg.draw.line(surf, GREEN, (int(CX - x), int(CY - y)),
                                  (int(CX - x2), int(CY - y2)))


def main():
    pg.init()
    surf = pg.display.set_mode(SIZE)
    pg.display.set_caption('heart')
    clock = pg.time.Clock()
    font = pg.font.SysFont('Arial', 20)
    factor = 1
    while True:
        draw(surf, font, clock.get_fps(), factor)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()
        clock.tick(FPS)
        factor += 0.001


if __name__ == '__main__':
    main()
