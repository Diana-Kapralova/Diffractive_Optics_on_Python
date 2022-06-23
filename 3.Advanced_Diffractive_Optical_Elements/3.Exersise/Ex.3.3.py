import numpy as np
from utils import plot_output

# Defining parameters
N = 500
L = 5  # Topological charge number
A3 = np.zeros((N, N), dtype='complex_')
# Constructing SPP
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
theta = np.arctan2((X - N/2), (Y - N/2))
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
A1 = L * (theta + np.pi)
A2 = np.fmod(A1, 2*np.pi)

for p in range(N):
    for q in range(N):
        if np.fmod(A2[p, q], 2*np.pi) <= np.pi:
            A3[p, q] = np.exp(1j * np.pi)
        else:
            A3[p, q] = np.exp(1j * 0)
A3[r > 30] = 0

plot_output(A3, N, angle=True, spiral=True)