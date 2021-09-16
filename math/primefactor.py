import sys

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return n, factors


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(*prime_factors(n))
    else:
        sys.stderr.write("Usage: prime-factors INTEGER\n")
        sys.exit(2)
