# Defining Grating Parameters
import numpy as np
from utils import plot_output

N = 500
A = np.ones((N, N))
r = np.ones((N, N))
# Period of gratings
P = 50
# Fill factor
FFr = 0.5
# Constracting the gratings
x = np.array([i for i in range(1, N+1)])
y = np.array([j for j in range(1, N+1)])
delim = 10
X, Y = np.meshgrid(x*delim, y*delim, indexing='xy')
r = np.sqrt((X - N/2*delim)*(X-N/2*delim) + (Y - N/2*delim)*(Y-N/2*delim))
A[np.remainder(r, P) < P/2] = np.exp(1j * np.pi)
A[r > (N/2 - 2)] = 0

plot_output(A, N)
