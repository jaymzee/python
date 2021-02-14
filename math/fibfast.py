import math

c1 = math.sqrt(5) / 5
c2 = -c1
l1 = (1 + math.sqrt(5)) / 2
l2 = (1 - math.sqrt(5)) / 2

def fib(n):
    return c1 * l1 ** n + c2 * l2 ** n

if __name__ == '__main__':
    print(fib(10))
