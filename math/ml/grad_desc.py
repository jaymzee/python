"""
batch gradient descent
"""

import numpy as np

m = 100             # number of samples
n = 2               # number of features
alpha = 1           # learning rate
threshold = 0.00001 # close enough
theta = np.zeros(n + 1) # parameters

# generate data set
X = np.vstack([np.ones(m), np.random.rand(n, m) * 1]).T
v = np.array([3.0, 1.5, 2.1])   #  y = 3.0 + 1.5 x1 + 2.1 x2
y = X @ v + np.random.normal(size=m, scale=0.1)

iterations = 0
while True:
    iterations += 1
    h = X @ theta
    delta = -alpha / m * (h - y) @ X
    theta += delta
    if np.linalg.norm(delta) < threshold:
        break

print(theta)
print("hypothesis computed in %d iterations using batch gradient descent" %
      iterations)
