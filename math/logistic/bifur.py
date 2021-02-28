"""
graph the bifurcation diagram of the logistic map
"""

import numpy as np
import matplotlib.pyplot as plt
from fixed import fixed_point
from logistic import logistic


rs = np.linspace(1.0, 4.0, 1000)
for r in rs:
    plt.scatter(r * np.ones(100),
                fixed_point(lambda x: logistic(r, x), 0.4, 200)[-100:],
                color='blue', s=1)
plt.ylim([0,1])
plt.xlim([1.0,4.0])
plt.show()
