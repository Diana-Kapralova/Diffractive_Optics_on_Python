import numpy as np
from utils import plot_output

# Defining FZP parameters
N = 500
f = 10000  # focal length in microns
lamb = 0.632  # wavelength in microns
g = 4
step = (2*np.pi)/g
C = np.zeros((N, N), dtype='complex_')
# Constructing the blazed FZP
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
# As 3.6.4-level_FZP but change one sign near f and formula for constructing
A = (f + np.sqrt(f * f + r * r)) * (2 * np.pi) / lamb
# Equivalent of function rem() in MATLAB
# is np.fmod(). NOT np.remainder()
B = np.fmod(A, 2*np.pi)
B[r > N/2] = 0

for p in range(N):
    for q in range(N):
        for n in range(g):
            if (B[p, q] > (n * np.pi/2)) and (B[p, q] <= (n + 1) * np.pi / 2):
                C[p, q] = np.exp(1j * (n + 1) * np.pi / 2)

plot_output(C, N, angle=True, profile=True)
