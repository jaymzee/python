"""
quaternions

    q = w + xi + yj + zk
    q* = w - xi - yj - zk

    i² = j² = k² = ijk = -1

norm of the quaternion

    ||q||² = w² + x² + y² + z² = q* q = q q*

a quaternion is called a unit quaternion when

    w² + x² + y² + z² = 1

a quaternion is called pure or a vector in R³ when w = 0

    v = v1 i + v2 j + v3 k

given two quaternions, the norm of the product is the product of the norms

the real part of the product of two quaternions pq is the same as the real
part of qp

what happens when you take a unit quaternion q and a pure quaternion v and
calculate

    p = q* v q

we have

    ||p|| = ||q*|| · ||v|| · ||q||
          =   1    · ||v|| ·   1
          = ||v||

but as to the real part,

    Re v = 0

then

    Re q*(vq) = Re (vq)q*
              = Re v(qq*)
              = Re v
              = 0

so p = q*vq is another pure quaternion, another vector, the same length as
v, but rotated from where it was.

"""

import numpy as np

def prod(q1, q0):
    """return the product of the quaternions q1 q0"""

    w0, x0, y0, z0 = q0
    w1, x1, y1, z1 = q1

    return np.array([-x1*x0 - y1*y0 - z1*z0 + w1*w0,
                      x1*w0 + y1*z0 - z1*y0 + w1*x0,
                     -x1*z0 + y1*w0 + z1*x0 + w1*y0,
                      x1*y0 - y1*x0 + z1*w0 + w1*z0])


def conj(q):
    """return the conjugate of the quaternion q"""

    return np.array([q[0], -q[1], -q[2], -q[3]])


def norm(q):
    """return the norm of the quaternion q
    ||q||² = w² + x² + y² + z²
    """

    return np.linalg.norm(q)


def rotate(q, v):
    """3D rotation using quaternions

    q unit quaternion
    v "vector" or "pure" quaternion

    returns the rotated "vector" p = q* v q
    """

    return prod(prod(conj(q), v), q)


def rot_q(theta, x, y, z):
    """return the quaternion q that represents a 3D rotation

    theta is the rotation angle in radians
    x, y, z is the unit axis (Euler axis) that the space will be rotated about.
    """
    s = np.sin(theta/2.0)
    c = np.cos(theta/2.0)
    q = np.array([c, s*x, s*y, s*z])
    return q / norm(q)


if __name__ == "__main__":
    print('2 · 3 = 6', prod([2,0,0,0], [3,0,0,0]))
    print('i² = -1', prod([0,1,0,0], [0,1,0,0]))
    print('j² = -1', prod([0,0,1,0], [0,0,1,0]))
    print('k² = -1', prod([0,0,0,1], [0,0,0,1]))
    print('ij =  k', prod([0,1,0,0], [0,0,1,0]))
    print('jk =  i', prod([0,0,1,0], [0,0,0,1]))
    print('ki =  j', prod([0,0,0,1], [0,1,0,0]))
    print('ji = -k', prod([0,0,1,0], [0,1,0,0]))
    print('kj = -i', prod([0,0,0,1], [0,0,1,0]))
    print('ik = -j', prod([0,1,0,0], [0,0,0,1]))
    print('ijk = -1', prod(prod([0,1,0,0], [0,0,1,0]), [0,0,0,1]))

    print('conj([1 2 3 4]) =', conj([1,2,3,4]))
    print('norm([1 2 3 4]) =', norm([1,2,3,4]))
