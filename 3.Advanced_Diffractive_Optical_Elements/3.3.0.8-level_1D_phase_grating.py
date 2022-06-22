import numpy as np
from utils import plot_output
import matplotlib.pyplot as plt

# Defining grating parameters

N = 500
P = 100
A1 = np.ones((P, N), dtype='complex_')  # Size of fundamental building block of grating
g = 8  # Number of phase levels
delphase = 2*np.pi/g  # Phase step size

# Constructing one n-level section of the phase grating
sub = np.round(P/g)
for count in range(g):
    # for each layer 25 indexes turn in phase value depending on delphase
    # (all phase delay for overall thickness should be 2pi -
    # input light should have the same phase as output light)
    A1[int(count * sub):int((count + 1)*sub), :] = np.exp(1j*count * delphase)
    k = A1[int(count * sub):int((count + 1)*sub), :]

# Constracting the full grating
A2 = np.tile(A1, (int(N/P), 1))

plot_output(A2, N, angle=True, profile=True)
