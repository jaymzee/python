import matplotlib.pyplot as plt
import numpy as np
from logistic import logistic

t = np.linspace(0, 10, 100)
plt.plot(t, logistic(1.0, 0.8, t), label=r'$ \frac{1}{1 + 0.25 e^{-rt}} $')
plt.plot(t, logistic(1.0, 0.5, t), label=r'$ \frac{1}{1 + e^{-rt}} $')
plt.plot(t, logistic(1.0, 1/4, t), label=r'$ \frac{1}{1 + 3 e^{-rt}} $')
plt.plot(t, logistic(1.0, 0.01, t), label=r'$ \frac{1}{1 + 99 e^{-rt}} $')
plt.ylim([0,1])
plt.grid()
plt.legend()
plt.xlabel(r'$ t $')
plt.title(r'logistic function $ x(t), r = 1 $')
plt.show()
