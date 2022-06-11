import numpy as np
from utils import plot_output

# Defining Axicon Parameters
N1 = 100  # Size of axicon
N2 = 500  # Size of matrix
ratio = N2/N1
A1 = np.zeros((N1, N1))
r = np.zeros((N1, N1))
# Period of axicon
P = 10

for p in range(N1):  # Generate the fundamental building block – single axicon
    for q in range(N1):
        # Create polar coordinate
        r[p, q] = np.sqrt((p - N1/2)*(p - N1/2) + (q - N1/2)*(q - N1/2))
        if r[p, q] < N1/2:
            if np.remainder(r[p,q], P) < P/2:
                A1[p, q] = 1

# Multiplying axicon the gratings - full grating
A2 = np.tile(A1, (int(ratio), int(ratio)))

plot_output(A2, N2)