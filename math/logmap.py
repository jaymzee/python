"""
logistic map
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

def logistic_seq(r, x0, N):
    xn = x0
    x = [x0]
    for n in range(N):
        xn = logistic(r, xn)
        x.append(xn)
    return np.array(x)

N = 20
plt.plot(logistic_seq(1.6, 0.4, N), marker='o', label='r = 1.6')
plt.plot(logistic_seq(2.6, 0.4, N), marker='o', label='r = 2.6')
plt.plot(logistic_seq(3.0, 0.4, N), marker='o', label='r = 3.0')
plt.plot(logistic_seq(3.7, 0.4, N), marker='o', label='r = 3.7')
plt.ylim([0,1])
plt.legend()
plt.show()
