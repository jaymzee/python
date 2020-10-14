import numpy as np

σ = [np.array([[0, 1],[1, 0]]),
    np.array([[0, -1j],[1j, 0]]),
    np.array([[1, 0],[0, -1]])]

x = []
for i in range(3):
    x.append(np.linalg.eig(σ[i])[1])

print('Pauli Matrices:')
for i in range(3):
    print("σ%d =\n%s\n" % (i + 1, σ[i]))

print('eigenvalues:\nλ = [1, -1]\n')
print('eigenvectors:')
for i in range(3):
    print('x%d =\n%s\n' % (i + 1, x[i]))
