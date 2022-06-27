import numpy as np
import matplotlib.pyplot as plt

N = 500
lamb = 0.633 * 10**(-6)
z1 = 0.025  # Propagation distance = 25 mm
z2 = 50  # and 50 m
P = 10**(-4)  # Radius of aperture = 0.1 mm
wsamp = 10 * lamb  # sampling period or width

# Creating sampled space
x = np.array([i for i in range(N)])
y = np.array([j for j in range(N)])

X, Y = np.meshgrid(x, y)
Rsamp = np.sqrt((X - N/2)**2 + (Y - N/2)**2) * wsamp # Define sampled radius

# Constructing the aperture
A = np.ones((N, N))  # Define matrix
A[np.fmod(Rsamp, P) < P/2] = np.exp(1j*np.pi)

# for different propagation distance
for z in [z1, z2]:
    # Calculating the Fresnel diffraction pattern
    PPF = np.exp(1j * np.pi/ (lamb * z) * Rsamp * Rsamp)  # Calculating the parabolic phase factor
    A1 = A * PPF  # Multiply the circular aperture function with the parabolic phase factor
    E = abs(np.fft.fftshift(np.fft.fft2(np.fft.fftshift(A1))))  # Calculating FT

    plt.figure(figsize=(8, 8))
    plt.imshow(E, cmap='gray')
    plt.figure(figsize=(8, 8))
    IN = abs(E) * abs(E)
    plt.plot(x, IN, c='gray')
    plt.show()