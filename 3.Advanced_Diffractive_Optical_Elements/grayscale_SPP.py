import numpy as np
from utils import plot_output

# Defining parameters
N = 500
L = 2  # Topological charge number

# Constructing SPP
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
theta = np.arctan2((X - N/2), (Y - N/2))
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
A1 = np.exp(1j * L * theta)
A1[r > 30] = 0

plot_output(A1, N, angle=True, spiral=True)