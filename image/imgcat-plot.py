"""
display matplotlib plot in the terminal (iTerm2 or mintty)

the backend for matplotlib can be set in the environment
to use imgcat
    MPLBACKEND="module://imgcat"
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.28, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.grid()
plt.legend()
plt.show()
