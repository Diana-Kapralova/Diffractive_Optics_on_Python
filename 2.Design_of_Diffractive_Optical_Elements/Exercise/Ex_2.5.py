import numpy as np
from utils import plot_output

# Elliptical FZP
# Define FZP parameters
N = 500  # matrix size
M = 20  # number of grating lines
A = np.ones((N, N))  # Define amplitude matrices with amplitude vale = 1
rx = np.zeros((M, M))  # matrices for creating grating lines
r = np.zeros((N, N))
# ratio equal to 1.5 according to the task
fx = 3000  # focal length in micrometers
fy = 4500
lamb = 0.633  # wavelength in micrometers

# Constracting FZP
for n in range(M):
    # equation for FZP width of grating lines
    rx[n] = np.sqrt(abs(n-1)*fx*lamb)

for n in range(0, M, 2):
    for p in range(N):
        for q in range(N):
            # create polar system of coordinates
            # (in this case one axes will be longer
            # for creation elliptical shape)
            r[p, q] = np.sqrt(((p - N/2)*(p - N/2)) * (fx/fy) + ((q - N/2)*(q - N/2)))
            if (np.all(r[p, q] > rx[n])) and (np.all(r[p, q] < rx[n+1])):
                # change amplitude by phase(phase FZP)
                A[p, q] = np.exp(1j*np.pi)

plot_output(A, N)