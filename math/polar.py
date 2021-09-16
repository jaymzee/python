import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
ax = plt.axes(projection="polar")
ax.set_rlim([0, 2])
ax.plot(theta, np.cos(theta), label="$ r = cos(\\theta) $")
ax.plot(theta, 1 + np.cos(theta), label="$ r = 1 + cos(\\theta) $")
ax.plot(theta, 0.25 * theta, label="$ r = 0.25 \\theta $")
plt.legend()
plt.show()
