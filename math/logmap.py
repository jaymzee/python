"""
logistic map
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x0, N):
    xn = x0
    x = [x0]
    for n in range(N):
        xn = r * xn * (1 - xn)
        x.append(xn)
    return np.array(x)

N = 20
plt.plot(logistic_map(1.6, 0.4, N), marker='o', label='r = 1.6')
plt.plot(logistic_map(2.6, 0.4, N), marker='o', label='r = 2.6')
plt.plot(logistic_map(3.2, 0.4, N), marker='o', label='r = 3.2')
plt.plot(logistic_map(3.7, 0.4, N), marker='o', label='r = 3.7')
plt.ylim([0,1])
plt.legend()
plt.show()
