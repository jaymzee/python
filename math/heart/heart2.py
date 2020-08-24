import sys
import time
import pygame as pg
import numpy as np

SIZE = (1000, 1000)         # window size
WIDTH, HEIGHT = SIZE        # window width and height
CX = WIDTH / 2              # center of window
CY = HEIGHT / 2             # center of window
R = 450                     # radius of circle
FPS = 10                    # frames per second
POINTS = 500                # number of points around circle
FACT_INIT = 0.0             # factor initial value
FACT_DIV = 1                # factor subdivisions (non-integer factor)
FACT_INCR = 1 / FACT_DIV    # increment for factor


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
    fps_text = font.render("%.1f fps" % fps, 0, YELLOW)
    fac_text = font.render("%.3f" % factor, 0, WHITE)
    surf.blit(fps_text, (10, 10))
    surf.blit(fac_text, (int(CX - R), int(CY / 4)))
    n1 = np.arange(POINTS)
    n2 = factor * n1
    theta = 2 * np.pi * n1 / POINTS
    phi = 2 * np.pi * n2 / POINTS
    x = CX - R * np.cos(theta)
    y = CY - R * np.sin(theta)
    x2 = CX - R * np.cos(phi)
    y2 = CY - R * np.sin(phi)
    for n in n1:
        pg.draw.line(surf, GREEN, (int(x[n]), int(y[n])),
                                  (int(x2[n]), int(y2[n])))


def main():
    pg.init()
    surf = pg.display.set_mode(SIZE)
    pg.display.set_caption('heart')
    clock = pg.time.Clock()
    font = pg.font.SysFont('Arial', 20)
    factor = FACT_INIT
    int_count = FACT_DIV  # frame counter for between integral vals of factor
    while True:
        if (FACT_DIV > 1 and int_count >= FACT_DIV):
            pause_after = True
            int_count = 0
        else:
            pause_after = False
        draw(surf, font, clock.get_fps(), factor)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()
        clock.tick(FPS)
        if pause_after:
            time.sleep(2.0)
        factor += FACT_INCR
        int_count += 1


if __name__ == '__main__':
    main()
