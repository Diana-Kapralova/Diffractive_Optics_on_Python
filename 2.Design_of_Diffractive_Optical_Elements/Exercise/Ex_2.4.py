import numpy as np
from utils import plot_output

# Parameters
# Here we use additionally XOR operation
# for creating crossing 2D plates
N = 500 # matrix size
M = 50 # Number of gratings lines
A1 = np.zeros((N, N))  # Need 2 amplitudes for crossing
A2 = np.zeros((N, N))
A = np.zeros((N, N))  # Resulting phase plates
x = np.zeros((M, M))
y = np.zeros((M, M))

# Different focal length for axes for diff condition
fx = 3000 # focal length
fy = 6000
lamb = 0.633 # wavelength in micrometers

# Constracting the FZP
for n in range(0, M):
    # Obtain the width of grating lines(diff because of diff f)
    x[n] = np.sqrt(n * fx * lamb)
    y[n] = np.sqrt(n * fy * lamb)

for n in range(0, M, 2):
    for p in range(0, N):
        for q in range(0, N):
            # Creating different masks for each grating length
            if (np.all(abs(q - N/2) > x[n])) and (np.all(abs(q-N/2) < x[n+1])):
                A1[p, q] = 1
            if (np.all(abs(p - N/2) > y[n])) and (np.all(abs(p-N/2) < y[n+1])):
                A2[p, q] = 1

# Create phase plates using XOR for masks
A = np.exp(1j * np.pi * np.logical_xor(A1, A2))

plot_output(A, N, angle=True)