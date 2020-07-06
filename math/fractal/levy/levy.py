import sys
import pygame as pg
from math import sqrt
from itertools import accumulate

# global parameters
SIZE = (1000, 800)
WIDTH, HEIGHT = SIZE
STARTP = (300, 250)
STARTD = 400
FPS = 10

# global contants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
PHI = (1 + sqrt(5)) / 2
SQRT2 = sqrt(2)

def curve(p1, d, s):
    """return an iterator of vertices that represent the curve string

       s  a string of single character commands to draw the curve
       d  distance moved by F command
       p1 initial vertex to start from

       string commands
       F move forward by d
       + rotate clockwise
       - rotate counterclockwise
    """

    dx = [1, 1/SQRT2,  0, -1/SQRT2, -1, -1/SQRT2,  0,  1/SQRT2]
    dy = [0, 1/SQRT2,  1,  1/SQRT2,  0, -1/SQRT2, -1, -1/SQRT2]
    a = 0
    x, y = p1
    yield (x, y)
    for c in s:
        if c == '+':
            a = (a + 1) % 8
        elif c == '-':
            a = (a - 1) % 8
        elif c == 'F':
            x += d * dx[a]
            y += d * dy[a]
            yield (x, y)


def levy(n, p1, d):
    """return a list of vertex lists representing levy curves"""
    ds = map(lambda i: d / SQRT2**i, range(n+1))
    ss = accumulate('F'*(n+1), lambda t, e: t.replace(e, '+F--F+'))
    return list(map(lambda args: list(curve(p1, *args)), zip(ds, ss)))


def draw(curve, n):
    surf.fill(BLACK)
    pg.draw.lines(surf, GREEN, False, curve)
    fps = clock.get_fps()
    fps_text = font.render("%6.1f fps" % fps, 0, YELLOW)
    surf.blit(fps_text, (0, 0))
    surf.blit(font.render('n = %d' % n, 0, YELLOW), (0, 20))


def main():
    global surf, font, clock

    n = 0
    curves = levy(16, STARTP, STARTD)
    pg.init()
    surf = pg.display.set_mode(SIZE)
    pg.display.set_caption('Levy C curve')
    clock = pg.time.Clock()
    font = pg.font.SysFont('Arial', 20)
    while True:
        if n < len(curves):
            draw(curves[n], n)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()
        n = (n + 1) % (len(curves) + 2 * FPS)
        clock.tick(FPS) #wait


if __name__ == '__main__':
    main()
