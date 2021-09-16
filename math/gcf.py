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


# g is the function to apply: min for gcf or max for lcm
def gcf_lcm(g, *nums):
    rslt = count(prime_factors(nums[0]))
    for m in nums:
        facts = count(prime_factors(m))
        # each factor is f^n
        rslt = {f: g(rslt[f], n) for f, n in facts.items() if f in rslt}
    return rslt


def usage():
    sys.stderr.write(f"Usage: {sys.argv[0]} integer_list\n")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        try:
            nums = [int(arg) for arg in sys.argv[1:]]
        except:
            usage();
            sys.exit(2)
        if 'gcf' in sys.argv[0]:
            print(gcf_lcm(min, *nums))
        else:
            print(gcf_lcm(max, *nums))
    else:
        usage()
        sys.exit(2)

