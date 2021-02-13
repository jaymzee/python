import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
ax = plt.axes(projection="polar")
ax.set_rlim([0, 2])
ax.plot(theta, np.cos(theta), label="$ r = cos(\\theta) $")
plt.legend()
plt.show()
