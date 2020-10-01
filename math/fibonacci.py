def fibs(n):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for i, v in enumerate(fibs(10)):
        print("fib(%d) = %d" % (i, v))

