import numpy as np

σ = [np.array([[0, 1],[1, 0]]),
    np.array([[0, -1j],[1j, 0]]),
    np.array([[1, 0],[0, -1]])]

x = [np.linalg.eig(m)[1] for m in σ]

print('Pauli Matrices:')
for i, m in enumerate(σ, 1):
    print("σ%d =\n%s\n" % (i, m))

print('eigenvalues:\nλ = [1, -1]\n')

print('eigenvectors:')
for i, v in enumerate(x, 1):
    print('x%d =\n%s\n' % (i, v))
