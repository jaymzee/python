import numpy as np

n = 8
f = lambda x: [x[0]**3 + x[1] - 1, -x[0] + x[1]**3 + 1]
Df = lambda x: [[3*x[0]**2, 1],[-1, 3*x[1]**2]]
x = [0.5, 0.5]

for i in range(n):
    x -= np.linalg.solve(Df(x), f(x))

print(x)
