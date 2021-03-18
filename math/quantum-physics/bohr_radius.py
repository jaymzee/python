import math

# SI constants
pi  = math.pi
h   = 6.62607004e-34    # plank's constant
ε_0 = 8.8541878128e-12  # vacuum permittivity
m_e = 9.10938356e-31    # electron mass (kg)
q_e = 1.60217662e-19    # electron charge
c =   2.99792458e8      # speed of light in vacuum (m/s)


def bohr_radius(n):
    return ε_0 * h*h * n*n/(pi * m_e * q_e*q_e)


def bohr_energy(n):
    return -m_e * q_e**4/(8 * (ε_0 * h * n)**2)

E = [bohr_energy(n) for n in range(1, 7)]
λ_lyman = [h * c / (En - E[0]) for En in E[1:]]

for i, λ in enumerate(λ_lyman):
    print("%d %g nm" % (i+2, λ * 1e9))

