
def nest(f, x0, N):
    xn = x0
    for n in range(N):
        xn = f(xn)
    return xn


def nest_list(f, x0, N):
    xn = x0
    x = [x0]
    for n in range(N):
        xn = f(xn)
        x.append(xn)
    return x


def fixed_point(f, x0):
    xn = x0
    while True:
        fxn = f(xn)
        if abs(fxn - xn) < 1E-9:
            break
        xn = fxn
    return xn


def fixed_point_list(f, x0):
    xn = x0
    x = [x0]
    while True:
        fxn = f(xn)
        if abs(fxn - xn) < 1E-9:
            break
        xn = fxn
        x.append(xn)
    return x
