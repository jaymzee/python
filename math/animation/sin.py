import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/ 50))
    return line,

ani = animation.FuncAnimation(
        fig, animate, interval=16, blit=True, save_count=50)

# to save animation, use e.g.
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#   fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
