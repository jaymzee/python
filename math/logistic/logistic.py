import numpy as np


def logistic_map(r, x):
    return r * x * (1 - x)


def logistic(r, x0, t):
    return 1 / (1 + (1 / x0 - 1) * np.exp(-r * t))
