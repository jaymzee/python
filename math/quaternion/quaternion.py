import numpy as np

def qmult(q1, q0):
    w0, x0, y0, z0 = q0
    w1, x1, y1, z1 = q1

    return np.array([-x1*x0 - y1*y0 - z1*z0 + w1*w0,
                      x1*w0 + y1*z0 - z1*y0 + w1*x0,
                     -x1*z0 + y1*w0 + z1*x0 + w1*y0,
                      x1*y0 - y1*x0 + z1*w0 + w1*z0])


if __name__ == "__main__":
    print(qmult([2,0,0,0], [3,0,0,0]), '2 * 3 =  6')
    print(qmult([0,1,0,0], [0,1,0,0]), 'i * i = -1')
    print(qmult([0,0,1,0], [0,0,1,0]), 'j * j = -1')
    print(qmult([0,0,0,1], [0,0,0,1]), 'k * k = -1')
    print(qmult(qmult([0,1,0,0], [0,0,1,0]), [0,0,0,1]), 'i * j * k = -1')
    print(qmult([0,1,0,0], [0,0,1,0]), 'i * j =  k')
    print(qmult([0,0,1,0], [0,0,0,1]), 'j * k =  i')
    print(qmult([0,0,0,1], [0,1,0,0]), 'k * i =  j')
    print(qmult([0,0,1,0], [0,1,0,0]), 'j * k = -k')
    print(qmult([0,0,0,1], [0,0,1,0]), 'k * j = -i')
    print(qmult([0,1,0,0], [0,0,0,1]), 'i * k = -j')
