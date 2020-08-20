import math

def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    sum = 0.0
    for i in range(0, n, 2):
        sum += f(x[i]) + 4*f(x[i+1]) + f(x[i+2])
    return h / 3.0 * sum

def f(x):
    return 2.0 / math.sqrt(math.pi) * math.exp(-x**2)

print("S(1.8) = ", simpsons_rule(f, 0.0, 1.8, 10))
print("erf(1.8) = ", math.erf(1.8))
print("S(.7) = ", simpsons_rule(f, 0.0, 0.7, 10))
print("erf(.7) = ", math.erf(.7))
