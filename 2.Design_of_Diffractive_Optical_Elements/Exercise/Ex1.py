import numpy as np
from utils import plot_output

# Copy code from 1d_phase_grating

# Define grating parameters
N = 500  # matrix size
A = np.ones((1, N))  # Define amplitude matrices with amplitude vale = 1
P = 100  # period of gratings
FF = 0.5  # fill factor
phase = 1.67  # Change phase parameter according to 0.5 changes of intensity

for q in range(N):
    if np.remainder(q, P) < P*FF:
        # Change phase parameter according to 0.5 changes of phase
        A[0, q] = np.exp(1j*phase)

A = np.tile(A, (N, 1))

plot_output(A, N, angle=True)