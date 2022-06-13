import numpy as np
from utils import plot_output
import matplotlib.pyplot as plt

# Defining gratings parameters
N = 500
P = 100
A1 = np.ones((P, N), dtype='complex_')

# Constructing the blazed axicon

x = np.array([i for i in range(N)])
y = np.array([i for i in range(N)])

X, Y = np.meshgrid(x, y)
r = np.sqrt((X - N/2) * (X - N/2) + (Y - N/2) * (Y - N/2))

# np.remainder cut radius into section blaze
# where P show period of this blades
A = np.exp(1j * (np.remainder(r, 20)) * (2 * np.pi)/P)
A[r > N/2] = 0
rem = np.remainder(r, 20)
plot_output(A, N, angle=True, profile=True)