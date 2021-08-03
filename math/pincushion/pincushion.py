import numpy as np
import matplotlib.pyplot as plt
import itertools

xx = np.linspace(0, 1, 10)
yy = np.linspace(0, 1, 10)

xx -= 0.5
yy -= 0.5

points = list(itertools.product(xx, yy))
xy = np.array(points).T

#plt.scatter(xy[0], xy[1])
#plt.show()

r = xy[0] ** 2 + xy[1] ** 2
xy /= (4 + r)

plt.scatter(xy[0], xy[1])
plt.show()
