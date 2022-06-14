import numpy as np
from utils import plot_output

# Defining parameters
N = 500
L = 1  # Topological charge number
g = 4  # Number of phase levels
delphase = (L*2*np.pi)/g

# Construct the SPP
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
theta = np.arctan2((X - N/2), (Y - N/2))
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))
A1 = np.array((L * theta + L * np.pi), dtype='complex_')
A1[r > 30] = 0

for n in range(g):
    for p in range(N):
        for q in range(N):
            if (A1[p, q] > (delphase*n)) and (A1[p, q] <= delphase*(n + 1)):
                A1[p, q] = np.exp(1j * delphase * n)

plot_output(A1, N, angle=True, spiral=True)

