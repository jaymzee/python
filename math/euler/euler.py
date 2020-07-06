import sys
import math
import pygame



size = (400, 400)
width, height = size
fps = 5

black  = (0, 0, 0)
red    = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green  = (0, 255, 0)
cyan   = (0, 255, 255)
blue   = (0, 0, 255)
purple = (255, 0, 255)
grey   = (64, 64, 64)

sf_n = 21     # number of slope fields
sf_r = 4      # radius of slope

def main():
    pygame.init()
    surf = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    plot_example_2(surf)

    #update display and wait for events
    pygame.display.flip()
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()


def plot_slope_field(surf, f):
    """
    plot a slope field for the given function

    Args:
        surf: drawing surface to plot to
        f: function to evaluate
    """
    xi = width / sf_n
    yi = height / sf_n
    xo = xi / 2.0
    yo = yi / 2.0
    cx = (width - 1) / 2.0
    cy = (height - 1) / 2.0

    # draw axis
    pygame.draw.line(surf, grey, (cx, 0), (cx, height))
    pygame.draw.line(surf, grey, (0, cy), (width, cy))

    # draw slope field
    for i in range(sf_n):
        for j in range(sf_n):
            x = j * 2.0 / (sf_n - 1) - 1.0
            y = 1.0 - i * 2.0 / (sf_n - 1)
            t = math.atan(f(x, y))
            dx = sf_r * math.cos(t)
            dy = sf_r * math.sin(t)
            pygame.draw.line(surf, grey,
                             (j * xi + xo - dx, i * yi + yo + dy),
                             (j * xi + xo + dx, i * yi + yo - dy))


def plot_euler(surf, f, x0, y0, xf, step, **kwargs):
    """
    plot a function using Euler's method

    Args:
        surf: drawing surface for plot
        f: function to plot
        x0: initial value of x
        y0: initial value of y
        xf: final value of x
        step: step size for x
        **kwargs:
            color: line color for plot
    """
    color = kwargs.get('color', red)
    xi = width / sf_n
    yi = height / sf_n
    xo = xi / 2.0
    yo = yi / 2.0
    while x0 < xf:
        y1 = y0 + step * f(x0, y0)
        x1 = x0 + step
        pygame.draw.line(surf, color,
                         ((x0 + 1.0) / 2.0 * (sf_n - 1) * xi + xo,
                          (1.0 - y0) / 2.0 * (sf_n - 1) * yi + yo),
                         ((x1 + 1.0) / 2.0 * (sf_n - 1) * xi + xo,
                          (1.0 - y1) / 2.0 * (sf_n - 1) * yi + yo))
        x0 = x1
        y0 = y1


def plot_example_hyperbolic(s):
    f = lambda x, y: x / y
    pygame.display.set_caption("Euler's method:  dy/dx = x/y")
    plot_slope_field(s, f)
    plot_euler(s, f, 0.3, 0.02, 1.0, 0.0001)
    plot_euler(s, f, -0.9, 1.0, 1.0, 0.0001)
    plot_euler(s, f, -0.98, -1.0, 1.0, 0.0001)


def plot_example_circular(s):
    f = lambda x, y: -x / y
    pygame.display.set_caption("Euler's method:  dy/dx = -x/y")
    plot_slope_field(s, f)
    plot_euler(s, f, -0.95,  0.1, 0.95, 0.0001, color=red)
    plot_euler(s, f, -0.95, -0.1, 0.95, 0.0001, color=green)


def plot_example_x_plus_y(s):
    f = lambda x, y: x + y
    pygame.display.set_caption("Euler's method:  dy/dx = x + y")
    plot_slope_field(s, f)
    plot_euler(s, f, -0.95, 0.20, 1, 0.0001, color=red)
    plot_euler(s, f, -0.95, 0.21, 1, 0.0001, color=yellow)
    plot_euler(s, f, -0.95, 0.22, 1, 0.0001, color=green)
    plot_euler(s, f, -0.95, 0.23, 1, 0.0001, color=cyan)


def plot_example_2(s):
    f = lambda x, y: x + y
    pygame.display.set_caption("Euler's method:  dy/dx = x + y")
    plot_slope_field(s, f)
    plot_euler(s, f, -0.6, 0.30, 0.8, 0.0001, color=green)
    plot_euler(s, f, -0.7, 0.30, 0.8, 0.0001, color=yellow)
    plot_euler(s, f, -0.8, 0.30, 0.9, 0.0001, color=orange)
    plot_euler(s, f, -0.9, 0.30, 0.9, 0.0001, color=red)
    plot_euler(s, f, -0.9, 0.20, 1.0, 0.0001, color=purple)
    plot_euler(s, f, -0.8, 0.10, 1.0, 0.0001, color=blue)
    plot_euler(s, f, -1.0, 0.20, 1.0, 0.0001, color=cyan)
    plot_euler(s, f, -0.7, -0.10, 1.0, 0.0001, color=green)


def plot_example_exponential(s):
    f = lambda x, y: y
    pygame.display.set_caption("Euler's method:  dy/dx = y")
    plot_slope_field(s, f)
    plot_euler(s, f, -0.95,  0.1, 0.95, 0.0001, color=red)
    plot_euler(s, f, -0.95, -0.1, 0.95, 0.0001, color=green)


def plot_example_nonlinear(s):
    f = lambda x, y: math.sqrt(abs(y))
    pygame.display.set_caption("Euler's method:  dy/dx = sqrt(|y|)")
    plot_slope_field(s, f)
    plot_euler(s, f, -0.95, -0.55, 1, 0.0001)
    plot_euler(s, f, -0.95, -0.60, 1, 0.0001)
    plot_euler(s, f, -0.95, -0.65, 1, 0.0001)
    plot_euler(s, f, -0.95, -0.70, 1, 0.0001)
    plot_euler(s, f, -0.95, -0.75, 1, 0.0001)
    plot_euler(s, f, -0.95, -0.80, 1, 0.0001)


if __name__ == '__main__':
    main()