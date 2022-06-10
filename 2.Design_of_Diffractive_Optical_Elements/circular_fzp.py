import numpy as np
from utils import plot_output

# Define FZP parameters
N = 1000  # matrix size
M = 50  # number of grating lines
A = np.ones((N, N))  # Define amplitude matrices with amplitude vale = 1
r1 = np.zeros((M, M))  # matrices for creating grating lines
r = np.zeros((N, N))
f = 3000  # focal length in micrometers
lamb = 0.633  # wavelength in micrometers

# Constracting FZP
for n in range(M):
    # equation for FZP lines
    r1[n] = np.sqrt(n*f*lamb)

for n in range(0, M, 2):
    for p in range(N):
        for q in range(N):
            # create polar system of coordinates
            r[p, q] = np.sqrt((p - N/2)*(p - N/2) + (q - N/2)*(q - N/2))
            if (np.all(r[p, q] > r1[n])) and (np.all(r[p, q] < r1[n+1])):
                # change amplitude by phase(phase FZP)
                A[p, q] = np.exp(1j*np.pi)
                print(p, q)
    print(n)

plot_output(A, N)

