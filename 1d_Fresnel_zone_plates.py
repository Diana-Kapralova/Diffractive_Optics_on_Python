import numpy as np
import matplotlib.pyplot as plt
from utils import norm_output
N = 500 # matrix size
M = 50 # Number of gratings lines
A = np.ones((N, N))
x = np.zeros((M, M))
f = 3000 # focal length of FZP in micromiters
lamb = 0.433 # wavelength in micrometers

# Constracting the FZP
for n in range(0, M):
    x[n] = np.sqrt(n * f * lamb)
for n in range(0, M, 2):
    for q in range(0, N):
        if (np.all(abs(q - N/2) > x[n])) and (np.all(abs(q-N/2) < x[n+1])):
            A[:, q] = np.exp(1j*np.pi)

norm_output(A, N)