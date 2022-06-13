import numpy as np
from utils import plot_output

# Defining gratings parameters
N = 500
P = 100
A1 = np.ones(P, N)

for p in range(P):
    A1[p, :] = np.exp(1j * (p/P) * 2 * np.pi)

A2 = np.tile(A1, (int(N/P), 1))

