import numpy as np
from utils import norm_output

# Define grating parameters
N = 500  # matrix size
A = np.ones((1, N))  # Define amplitude matrices with amplitude vale = 1
P = 100  # period of gratings
FF = 0.5  # fill factor

for q in range(N):
    if np.remainder(q, P) < P*FF:
        A[0, q] = np.exp(1j*np.pi)

A = np.tile(A, (N, 1))

norm_output(A, N, angle=True)
