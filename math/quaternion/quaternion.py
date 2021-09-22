"""
quaternions

q = w + x i + y j + z k

"""

import numpy as np

def qmult(q1, q0):
    w0, x0, y0, z0 = q0
    w1, x1, y1, z1 = q1

    return np.array([-x1*x0 - y1*y0 - z1*z0 + w1*w0,
                      x1*w0 + y1*z0 - z1*y0 + w1*x0,
                     -x1*z0 + y1*w0 + z1*x0 + w1*y0,
                      x1*y0 - y1*x0 + z1*w0 + w1*z0])

def qconj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])

def qnorm(q):
    w, x, y, z = q
    return w*w + x*x + y*y + z*z


if __name__ == "__main__":
    print(qmult([2,0,0,0], [3,0,0,0]), '2 · 3 = 6')
    print(qmult([0,1,0,0], [0,1,0,0]), 'i² = -1')
    print(qmult([0,0,1,0], [0,0,1,0]), 'j² = -1')
    print(qmult([0,0,0,1], [0,0,0,1]), 'k² = -1')
    print(qmult(qmult([0,1,0,0], [0,0,1,0]), [0,0,0,1]), 'i j k = -1')
    print(qmult([0,1,0,0], [0,0,1,0]), 'i j = k')
    print(qmult([0,0,1,0], [0,0,0,1]), 'j k = i')
    print(qmult([0,0,0,1], [0,1,0,0]), 'k i = j')
    print(qmult([0,0,1,0], [0,1,0,0]), 'j i = -k')
    print(qmult([0,0,0,1], [0,0,1,0]), 'k j = -i')
    print(qmult([0,1,0,0], [0,0,0,1]), 'i k = -j')

    print('conj([1 2 3 4]) =', qconj([1,2,3,4]))
    print('norm([1 2 3 4]) =', qnorm([1,2,3,4]))
