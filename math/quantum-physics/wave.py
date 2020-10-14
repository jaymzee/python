import sys
import pygame as pg
import numpy as np
import cmath

def make_hsv_color(h, s, v):
    c = pg.Color(0)
    c.hsva = h, s, v, 100.0
    return c

def phase_to_color(angle):
    deg = 180 / pi * angle
    p = round(deg) % 360 #  0 <= p < 360
    return pcolor[p]

def plot_mag(y):
    xx = 50
    for v in y:
        vm, vp = cmath.polar(v)
        vy = 20 * vm ** 2
        c = phase_to_color(vp)
        pg.draw.line(surf, c, (int(xx), int(150)), (int(xx), int(150 - vy)))
        xx += 10
    pg.draw.line(surf, red, (50, 150), (xx, 150))

def plot_vec(y):
    xx = 50
    yy = 350
    for v in y:
        vx = 40 * v.real
        vy = 40 * v.imag
        c = phase_to_color(cmath.phase(v))
        pg.draw.line(surf, c, (xx, yy), (int(xx + vx), int(yy - vy)))
        xx += 10
        yy -= 5
    pg.draw.line(surf, red, (50, 350), (xx, yy))

def draw():
    #x = np.arange(0, 1, 1 / 32)
    x = np.arange(-3, 3, 6 / 32)
    #y = np.exp(1j*(2*np.pi/1.0*x - 1.0*2*np.pi*t))
    #y1 = 1 * np.exp(-0.1j * tpi * t) * np.sin(tpi / 2.0 * x)
    #y2 = 0.5 * np.exp(-0.4j * tpi * t) * np.sin(tpi / 1.0 * x)
    #y3 = 0.25 * np.exp(-0.9j * tpi * t) * np.sin(tpi / 0.5 * x)

    y0 = 0.8932 * np.exp(-x**2 - (1j/2) * t)
    y1 = 0.8932 * (2*x)*np.exp(-x**2 - (3j/2) * t)
    y2 = 0.5157 * (4*x**2 - 2)*np.exp(-x**2 - (5j/2) * t)
    #y3 = 0.2306 * (8*x**3 - 12*x)*np.exp(-x**2 - (7j/2) * t)

    plot_mag(y0 + y1 + y2)
    plot_vec(y0)
    plot_vec(y1)
    plot_vec(y2)
    #plot2(y3)

# setup pygame
fps = 60
size = (400, 400)
#size = (1280, 1024)
width, height = size
pg.init()
surf = pg.display.set_mode(size)
#surf = pg.display.set_mode(size, pg.FULLSCREEN)
pg.mouse.set_visible(0)
pg.display.set_caption('wave function')
clock = pg.time.Clock()

# setup some other globals and constants
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
t = 0.0         # elapsed time in seconds
pcolor = [make_hsv_color(i, 100.0, 100.0) for i in range(360)]
pi = np.pi
tpi = 2.0 * pi
pi2 = pi / 2.0
pi4 = pi / 4.0

while True: # main game loop
    surf.fill(black)
    draw()
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN:
            pg.quit()
            sys.exit()
    clock.tick(fps) #wait
    t += clock.get_time() / 1000
