import numpy as np
from utils import plot_output

# As 3.3.0.8_1D_phase grating but with g =16

# Defining grating parameters

N = 500
P = 100
A1 = np.ones((P, N), dtype='complex_')  # Size of fundamental building block of grating
g = 16  # Number of phase levels
delphase = 2*np.pi/g  # Phase step size

# Constructing one n-level section of the phase grating
sub = np.round(P/g)
for count in range(g):
    A1[int(count * sub):int((count + 1)*sub), :] = np.exp(1j*count * delphase)
    k = A1[int(count * sub):int((count + 1)*sub), :]

# Constracting the full grating
A2 = np.tile(A1, (int(N/P), 1))

# calculating efficiency of grating
m = 1  # first order of diffraction
efficiency = (abs(np.sin(m * np.pi/g) / (m*np.pi/g)))**2
print("Efficiency of", g, "- level grating = ", efficiency * 100, '%')

plot_output(A2, N, angle=True, profile=True)
