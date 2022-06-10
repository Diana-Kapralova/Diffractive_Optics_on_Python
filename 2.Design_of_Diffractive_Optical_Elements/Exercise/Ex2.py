import numpy as np
from utils import plot_output

# Use checkerboard.py
# Defining Grating Parameters
N = 500
# Need phase checkerboard for implementing exercise
F1 = np.zeros((N, N))
F2 = np.zeros((N, N))
A = np.zeros((N, N))
# Define the periods of the gratings
Px = 100
Py = 100
# Define fill factors
FFx = 0.5
FFy = 0.5

# Constracting the grating
for p in range(N-1, 1, -1):
    for q in range(1, N):
        if np.remainder(q, Px) < Px*FFx:
            # Change amplitude to phase mask(checkerboard) according
            # to solution for equal intensity in 3x3 spots
            F1[p, q] = 2.01
        if np.remainder(p, Py) < Py*FFy:
            F2[p, q] = 2.01


F_mask = np.add(F1, F2)
# Instead of implementing amplitude, we already need phase mask
# that's why pi disappear and F_mask appear
A = np.exp(1j*F_mask)

plot_output(A, N, angle=True)
