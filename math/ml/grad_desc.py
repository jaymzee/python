"""
batch gradient descent
"""

import numpy as np

def batch_gradient_descent(h, θ, X, y, **kwargs):
    α = kwargs.get("alpha", 0.01)
    threshold = kwargs.get("threshold", 0.001)
    n, d = 0, 1e8
    while np.linalg.norm(d) > threshold:
        d = α * (y - h(θ, X)) @ X
        n += 1
        θ += d  # modifies θ like a reference parameter
    return n


# generate data set
m = 10000               # number of samples
n = 2                   # number of features
X = np.vstack([np.ones(m), np.random.rand(n, m) * 1.0]).T
c = np.array([3.0, 1.5, 2.1])   #  y = 3.0 + 1.5 x1 + 2.1 x2
y = X @ c + np.random.normal(size=m, scale=0.1)

# determine parameters using data set and batch gradient descent
theta = np.zeros(n + 1) # initialize parameters
iterations = batch_gradient_descent(
    lambda θ, x: np.inner(θ,x),
    theta, X, y,
    alpha=1/m,
    threshold=1E-9
)
print("hypothesis computed in %d iterations using batch gradient descent" %
      iterations)
print(theta)
