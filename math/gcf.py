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
    return factors


def count(xs):
    S = set(xs)
    return S, {x: xs.count(x) for x in S}


if __name__ == "__main__":
    if len(sys.argv) > 2:
        args = sys.argv[1:]
        n = int(args[0])
        factors, counts = count(prime_factors(n))
        for arg in args[1:]:
            nfact, ncount = count(prime_factors(int(arg)))
            factors = factors.intersection(nfact)
            counts = {f: min(counts[f], c) for f, c in ncount.items() if f in counts}
        print(factors, counts)
    else:
        sys.stderr.write("Usage: gcf integer_list\n")
        sys.exit(2)

