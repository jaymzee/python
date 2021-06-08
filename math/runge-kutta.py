import numpy as np
import matplotlib.pyplot as plt

def rk4(f, t, y):
    for n, tn in enumerate(t[:-1]):
        h = t[n+1] - tn
        hh = h / 2.0
        yn = y[n]
        k1 = f(tn, yn)
        k2 = f(tn + hh, yn + k1 * hh)
        k3 = f(tn + hh, yn + k2 * hh)
        k4 = f(tn + h, yn + k3 * h)
        y[n+1] = yn + h / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


def euler(f, t, y):
    for n, tn in enumerate(t[:-1]):
        h = t[n+1] - tn
        y[n+1] = y[n] + h * f(tn, y[n])


t_rk = np.linspace(0.0, 2.0, 5)
t_ac = np.linspace(0.0, 2.0, 50)
y_rk = np.zeros(len(t_rk))
y_rk[0] = 1.0
y_ac = np.exp(-t_ac)
rk4(lambda t, y: -y, t_rk, y_rk)
plt.plot(t_rk, y_rk, '.', label='rk4')
plt.plot(t_ac, y_ac, label='actual')
plt.legend()
plt.show()
