"""
graph the bifurcation diagram of the logistic map
"""

import numpy as np
import matplotlib.pyplot as plt
from fixed import nest_list
from logistic import logistic_map


rs = np.linspace(1.0, 4.0, 1000)
for r in rs:
    plt.scatter(r * np.ones(100),
                nest_list(lambda x: logistic_map(r, x), 0.4, 200)[-100:],
                color='blue', s=1)
plt.ylim([0,1])
plt.xlim([1.0,4.0])
plt.show()
