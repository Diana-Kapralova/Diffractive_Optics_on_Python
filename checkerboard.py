import numpy as np
from ttictoc import tic, toc
import matplotlib.pyplot as plt
# Defining Grating Parameters
N = 500
A1 = np.zeros((N, N))
A2 = np.zeros((N, N))
A = np.zeros((N, N))
# Define the periods of the gratings
Px = 100
Py = 100
# Define fill factors
FFx = 0.5
FFy = 0.5
# Constracting the grating
tic()
for p in range(N-1, 1, -1):
    for q in range(1, N):
        if np.remainder(q, Px) < Px*FFx:
            A1[p, q] = 1
        if np.remainder(p, Py) < Py*FFy:
            A2[p, q] = 1

A = np.exp(1j*np.pi*np.logical_xor(A1, A2))
toc()

# Far field
E = np.fft.fftshift(np.fft.fft2(A))

# Intensity
IN = (np.abs(E)/(N*N))*(np.abs(E)/(N*N))

fig1 = plt.figure(figsize=(6, 6))
plt.imshow(np.angle(A), cmap='gray')
fig2 = plt.figure(figsize=(6, 6))
plt.imshow(IN, cmap='gray')
plt.show()
