import numpy as np
import matplotlib.pyplot as plt

N = 500
lamb = 0.633 * 10**(-6)
wsamp = 10**(-6)
x = np.array([i for i in np.arange(-N/2, N/2)])
y = np.array([j for j in np.arange(-N/2, N/2)])
X, Y = np.meshgrid(x * wsamp, y * wsamp)
Rsamp = np.sqrt(X**2 + Y**2)

f0 = 0.005  # Focal length
depth_f = 0.003  # Focal depth
R = 10**(-3)

# Design of axilens
f = (f0 + (depth_f/R) * np.sqrt(X**2 + Y**2))  # Focal length calculation
FZA = np.exp(-1j * (np.pi/lamb)*((X**2 + Y**2)/f))  # Phase profile of axilens

# Calculation of Fresnel diffraction pattern
m = 100
n = np.array([k for k in np.arange(1, m + 1)])

zs2 = 0.003 + (0.005/m) * n  # propagation distance
PPF = np.zeros((N, N, m), dtype='complex_')
A1 = np.zeros((N, N, m))
E = np.zeros((N, N, m))
field1 = np.zeros((100, m))
for counter1 in np.arange(0, m, 1):
    PPF[:, :, counter1] = np.exp(1j * np.pi/(lamb * zs2[counter1]) * Rsamp * Rsamp)  # Parabolic phase factor
    A1[:, :, counter1] = FZA * PPF[:, :, counter1]  # Multiply the axilens function with parabolic phase factor
    E[:, :, counter1] = abs(np.fft.fftshift(np.fft.fft2(np.fft.fftshift(A1[:, :, counter1]))))

    # Calculate Fourier Transform
    plt.imshow(E[200:300, 200:300, counter1], cmap='gray')
    plt.title('Propagation distance ' + str(round(zs2[counter1], 4) * 1000) + ' mm')
    plt.draw()
    plt.pause(0.5)
    plt.clf()

    field1[:, counter1] = E[int(N/2) + 1, 200:300, counter1]  # Accumulate the intensity profile

plt.imshow(field1, cmap='gray')
plt.show()