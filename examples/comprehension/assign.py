# Python 3.8 has a new assignment operator

nums = [y for x in range(20) if (y := x * x) <= 100]
print(nums)
