"""
stochastic gradient descent
"""

import numpy as np

def stochastic_gradient_descent(h, θ, X, y, **kwargs):
    α = kwargs.get('alpha', 0.01)
    threshold = kwargs.get('threshold', 0.0001)
    iterations = 0
    while True:
        θ_ = θ.copy()
        for i in range(len(X)):
            iterations += 1
            xi = X[i,:]
            θ -= α * (h(θ,xi) - y[i]) * xi
        if np.linalg.norm(θ - θ_) < threshold:
            break
    return iterations


# generate data set
m = 10000           # number of samples
n = 5               # number of features
X = np.vstack([np.ones(m), np.random.rand(n, m) * 1]).T
v = np.array([3.0, 1.5, 2.1, 3.14, 2.712, 1.0])
y = X @ v + np.random.normal(size=m, scale=0.1)

# compute parameters from data set using stochastic gradient descent
theta = np.zeros(n + 1) # parameters
iterations = stochastic_gradient_descent(
    lambda θ, x: x @ θ,
    theta, X, y,
    alpha=0.01,
    threshold=1E-9
)

print("hypothesis computed in %d iterations using stochastic gradient descent"
      % iterations)
print(theta)
