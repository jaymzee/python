"""
find zero of a function using Newton's method
"""

import numpy as np

def newton(f, Df, x0, epsilon, maxiter):
    x = x0
    for n in range(maxiter):
        fx = f(x)
        if abs(fx) < epsilon:
            return x, n
        Dfx = Df(x)
        if Dfx == 0:
            return None, n  # No solution
        x -= fx / Dfx
    return None, maxiter    # max iterations exceeded

def print_result(f, x, n):
    if x is not None:
        print("f(%g) = %g in %d iterations" % (x, f(x), n))
    else:
        print("no solution found after %d iterations" % n)

print("\nf(x) = cos(x)")
f = lambda x: np.cos(x)
Df = lambda x: -np.sin(x)
x, n = newton(f, Df, 1.0, 1e-13, 200)
print_result(f, x, n)

p = np.poly1d([1,3,2])
Dp = p.deriv()
print("       %s" % str(p).replace('\n', '\nf(x) = '))
x, n = newton(p, Dp, -5, 1e-9, 200)
print_result(f, x, n)
x, n = newton(p, Dp, 5, 1e-9, 200)
print_result(f, x, n)
