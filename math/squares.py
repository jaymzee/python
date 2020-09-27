# compute a table of squares using only addition
# (x+1)^2 = x^2 + 2x + 1
y = 0
for x in range(13):
    print("%2d^2 = %3d" % (x, y))
    y += x
    y += x
    y += 1
