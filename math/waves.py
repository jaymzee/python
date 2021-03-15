import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x = np.linspace(0, np.pi*4, 100)
line1, line2, line3 = plt.plot(x, 2*np.sin(x), x, 0*x, x, 0*x)
fig = plt.gcf()

def animate(frame):
    t = frame / 60.0
    y1 = np.sin(4.0 * x - 6.28 * 1.0 * t)
    y2 = np.sin(3.0 * x - 6.28 * 0.8 * t)
    line1.set_ydata(0*y1)
    line2.set_ydata(0*y2)
    line3.set_ydata(1*(y1 + y2))
    return line1, line2, line3

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
