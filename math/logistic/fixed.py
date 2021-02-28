import numpy as np


def fixed_point(f, x0, N):
    xn = x0
    x = [x0]
    for n in range(N):
        xn = f(xn)
        x.append(xn)
    return np.array(x)

