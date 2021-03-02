"""
plot logistic map
"""

import matplotlib.pyplot as plt
from fixed import nest_list
from logistic import logistic_map


def f(r, x0, N):
    return nest_list(lambda x: logistic_map(r, x), x0, N)


N = 20
plt.plot(f(1.6, 0.4, N), marker='o', label='r = 1.6')
plt.plot(f(2.6, 0.4, N), marker='o', label='r = 2.6')
plt.plot(f(3.0, 0.4, N), marker='o', label='r = 3.0')
plt.plot(f(3.7, 0.4, N), marker='o', label='r = 3.7')
plt.ylim([0,1])
plt.legend()
plt.show()
