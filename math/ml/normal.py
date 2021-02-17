"""
normal equation / ordinary least squares (OLS) / linear regression
"""

import numpy as np

m = 10   # samples
n = 2       # features

# generate data set
x = np.random.rand(n, m) * 10
y = 1.0 + 1.5 * x[0] + 2.1 * x[1] + np.random.normal(size=m)

# design matrix
A = np.vstack([np.ones(m), x]).T

# compute solution
xs = np.linalg.solve(A.T @ A, A.T @ y)

# print results
print("y = 1.0 + 1.5 x0 + 2.1 x1 + e(n)")
print("Ax* = y")
print("x* = %s" % xs)

print(y)
