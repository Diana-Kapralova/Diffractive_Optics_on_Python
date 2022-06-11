import numpy as np
from utils import plot_output

# Defining Grating Parameters
N = 500
# Define the periods of the gratings
P = 150
# Define fill factors
FF = 0.9

# Nt patterns of triangle with fill space(define by FF) and 0 pixels
Nt = P
At = np.ones((Nt, Nt))
for q in range(0, int(Nt)):
    for p in range(0, Nt):
        # Necessary condition for triangle
        if (p + q) >= Nt*FF - 1:
            At[p][q] = 0

# Rotate At for original triangle(not necessary)
At = np.rot90(At)

# Copy patterns N/Nt times
A = np.tile(At, (int(N / Nt), int(N / Nt)))

plot_output(A, N)
