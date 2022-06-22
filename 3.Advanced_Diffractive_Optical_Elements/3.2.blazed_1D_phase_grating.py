import numpy as np
from utils import plot_output
import matplotlib.pyplot as plt

# Defining gratings parameters
N = 500
P = 100
A1 = np.ones((P, N), dtype='complex_')

for p in range(P):
    A1[p, :] = np.exp(1j * (p/P) * 2 * np.pi)
plt.plot(A1)
A2 = np.tile(A1, (int(N/P), 1))

plot_output(A2, N, angle=True, profile=True)

