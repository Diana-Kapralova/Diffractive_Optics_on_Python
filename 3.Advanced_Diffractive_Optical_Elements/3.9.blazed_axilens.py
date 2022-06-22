import numpy as np
from utils import plot_output

# Defining parameters
N = 500
f0 = 5000  # focal length
delf = 1000  # focal depth
R = 1000  # radius of the element
lamb = 0.632

# Constracting the axilens
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
f = f0 + (delf/R)*r  # focal length equation
A = (f - np.sqrt(f*f + r*r)) * (2 * np.pi)/lamb
B = np.exp(1j * np.fmod(A, 2*np.pi))
B[r > N/2] = 0

plot_output(B, N, angle=True, profile=True)