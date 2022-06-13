import numpy as np
from utils import plot_output

# Defining axicon parameters
N = 480
A = np.zeros((N, N))
P = 40
g = 8
w = P/g  # width of each phase level
delphase = 2*np.pi/g

# Constructing the 8-level axicon
x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
r = np.sqrt((X - N/2)*(X - N/2) + (Y - N/2)*(Y - N/2))

for n in range(g):
    A[np.remainder(r + (n-1) * w, P) < P/g] = np.exp(1j * (w - n) * delphase)

A[r > N/2] = 0
plot_output(A, N, angle=True, profile=True)


