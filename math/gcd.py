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
    return {x: xs.count(x) for x in S}


def gcd(*nums):
    rslt = count(prime_factors(nums[0]))
    for m in nums:
        facts = count(prime_factors(m))
        # each factor is f^n
        rslt = {f: min(rslt[f], n) for f, n in facts.items() if f in rslt}
    return rslt


def lcm(*nums):
    rslt = count(prime_factors(nums[0]))
    for m in nums:
        facts = count(prime_factors(m))
        # each factor is f^n
        for f, n in facts.items():
            rslt[f] = max(n, rslt.get(f, 0))
    return rslt


def usage():
    sys.stderr.write(f"Usage: {sys.argv[0]} integer_list\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            nums = [int(arg) for arg in sys.argv[1:]]
        except:
            usage();
            sys.exit(2)
        if 'gcd' in sys.argv[0]:
            factors = gcd(*nums)
        else:
            factors = lcm(*nums)
        total = 1
        for f, n in factors.items():
            total *= f**n
        print(factors, total)
    else:
        usage()
        sys.exit(2)

