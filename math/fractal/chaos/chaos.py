import sys
import random
from math import sqrt, sin, cos, pi
import pygame as pg

# setup pygame
size = (924, 800)
#size = (1024, 1024)
#size = (1280, 1024)
width, height = size
pg.init()
surf = pg.display.set_mode(size)
#surf = pg.display.set_mode(size, pg.FULLSCREEN)
pg.mouse.set_visible(0)
pg.display.set_caption('chaos game')
clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 12)

# global constants
FPS = 60
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PHI = (1 + sqrt(5)) / 2

triangle = { 'vtxlist': [(width // 2, 0), (0, height), (width, height)],
             'factor': 1/2 }

vicsek = { 'vtxlist': [(0,0), (width,0), (width,height), (0,height),
                    (width//2,height//2)],
           'factor': 2/3 }

carpet = { 'vtxlist': [(0,0), (width,0), (width,height), (0,height),
                    (width//2,0), (width,height//2), (width//2,height),
                    (0,height//2)],
           'factor': 2/3 }

pentagon = { 'vtxlist': list(map(lambda n:
                          (width//2 + height//2 * sin(n*2*pi/5),
                           height//20 + height//2 * (1-cos(n*2*pi/5))),
                           range(5))),
             'factor': 1/PHI }

def sierpinski(p, vtxlist, factor):
    # select a vertex at random
    n = int(len(vtxlist) * random.random())
    v = vtxlist[n]
    # move a factor of the distance to that vertex
    dx = (v[0] - p[0]) * factor
    dy = (v[1] - p[1]) * factor
    return int(p[0] + dx), int(p[1] + dy)

def draw_fps():
    fps = clock.get_fps()
    fps_text = font.render("%6.2f fps" % fps, 0, RED)
    surf.blit(fps_text, (0,0))

def draw():
    p = width // 2, height // 2
    for i in range(10000):
        if (i > 5): # we throw away the first few points
            surf.set_at(p, GREEN)
        p = sierpinski(p, **pentagon)
    draw_fps()

def main():
    while True:
        surf.fill(BLACK)
        draw()
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()
        clock.tick(FPS) #wait

if __name__ == '__main__':
    main()

