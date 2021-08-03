import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

axcolor = 'lightgoldenrodyellow'

def f(n, v):
    x = np.linspace(-1, 1, n)
    y = np.linspace(-1, 1, n)
    points = itertools.product(x, y)
    xy = np.array(list(points)).T
    r = xy[0] ** 2 + xy[1] ** 2
    xy /= (v + r)
    xy *= v
    return xy


def main():
    def update(val):
        sc.set_offsets(f(10, val).T)

    distortion_init = 4
    xy = f(10, distortion_init)
    sc = plt.scatter(xy[0], xy[1])
    plt.title('pincushion distortion')
    plt.subplots_adjust(bottom=0.25)

    distortion = Slider(
        ax=plt.axes([0.25, 0.1, 0.65, 0.05], facecolor=axcolor),
        label='distortion',
        valmin=2.0,
        valmax=30,
        valinit=distortion_init,
    )
    distortion.on_changed(update)
    plt.show()

main()
