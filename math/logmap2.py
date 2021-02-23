"""
graph logistic map for different values of r
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

N = 100
tail = 20

r = np.linspace(1.0, 4.0, 200)
for rj in r:
    plt.scatter(rj * np.ones(tail),
                logistic_map(rj, 0.4, N)[N-tail:N],
                color='blue', marker='.')
plt.ylim([0,1])
plt.xlim([1,4])
plt.show()
