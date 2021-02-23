"""
graph the bifurcation diagram of the logistic map
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


rs = np.linspace(1.0, 4.0, 1000)
for r in rs:
    plt.scatter(r * np.ones(100),
                logistic_seq(r, 0.4, 200)[-100:],
                color='blue', s=1)
plt.ylim([0,1])
plt.xlim([1.0,4.0])
plt.show()
