import numpy as np
from utils import plot_output

# similar to 3.9.blazed_axilens
# Defining parameters
N = 500
f = 2000  # focal length
r0 = 100  # radius of the element
lamb = 0.632

# Constracting the axilens
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
A = (f - np.sqrt(f*f + (r - r0)*(r - r0))) * (2 * np.pi)/lamb
B = np.exp(1j * np.fmod(A, 2*np.pi))

plot_output(B, N, angle=True, profile=True)