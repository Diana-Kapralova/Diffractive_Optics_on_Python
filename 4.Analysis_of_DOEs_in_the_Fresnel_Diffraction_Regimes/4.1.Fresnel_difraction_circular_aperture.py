import numpy as np
import matplotlib.pyplot as plt

# Defining the parameters
N = 500
lamb = 0.633 * 10**(-6)  # Define wavelength in meters
z = 0.02  # Propagation distance = 20 mm
r = 10**(-3)  # Radius of aperture = 1 mm
wsamp = 10 * lamb  # sampling period width

# Creating sampled space
x = np.array([i for i in range(N)])
y = np.array([j for j in range(N)])

X, Y = np.meshgrid(x, y)
Rsamp = np.sqrt((X - N/2)**2 + (Y - N/2)**2) * wsamp # Define sampled radius

# Constructing the aperture
A = np.ones((N, N))
A[Rsamp >= r] = 0

# Calculating the Fresnel diffraction pattern
PPF = np.exp(1j * np.pi/(lamb * z) * Rsamp * Rsamp)  # Calculating the parabolic phase factor
# parabolic phase factor
A1 = A * PPF  # Multiply the circular aperture function with the parabolic phase factor
E = abs(np.fft.fftshift(np.fft.fft2(np.fft.fftshift(A1))))  # Calculating Fourier Transform

plt.imshow(E, cmap='gray')
plt.show()