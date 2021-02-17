"""
stochastic gradient descent
"""

import numpy as np

m = 10000           # number of samples
n = 5               # number of features
alpha = .01         # learning rate
threshold = 1E-9    # close enough
theta = np.zeros(n + 1) # parameters

# generate data set
X = np.vstack([np.ones(m), np.random.rand(n, m) * 1]).T
v = np.array([3.0, 1.5, 2.1, 3.14, 2.712, 1.0])
y = X @ v + np.random.normal(size=m, scale=0.1)

iterations = 0
while True:
    theta_old = theta.copy()
    for i in range(m):
        iterations += 1
        h = X[i,:] @ theta
        theta -= alpha * (h - y[i]) * X[i,:]
    if np.linalg.norm(theta - theta_old) < threshold:
        break

print(theta)
print("hypothesis computed in %d iterations using stochastic gradient descent"
      % iterations)
