import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib import animation

P = scipy.stats.norm()
N = 100000
x = P.rvs(N)
H, bins = np.histogram(x, bins=50)
bar = plt.bar(bins[:-1], H, width=.2)
plt.grid()
plt.ylim([0, 8000])
plt.xlim([-5, 5])
fig = plt.gcf()

def animate(frame):
    x = P.rvs(N)
    H, bins = np.histogram(x, bins=50)
    for i, b in enumerate(bar):
        b.set_height(H[i])
        b.set_x(bins[i])
    return bar

ani = animation.FuncAnimation(
        fig, animate, interval=33, blit=True, save_count=50)

# to save animation, use e.g.
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#   fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
