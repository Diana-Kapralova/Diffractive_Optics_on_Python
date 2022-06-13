import numpy as np
from utils import plot_output

# Defining FZP parameters
N = 500
f = 10000  # focal length in microns
lamb = 0.632  # wavelength in microns

# Constructing the blazed FZP
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
A = np.exp(1j * (f - np.sqrt(f * f + r * r)) * (2 * np.pi) / lamb)
A[r > N/2] = 0

plot_output(A, N, angle=True, profile=True)