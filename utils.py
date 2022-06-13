import numpy as np
import matplotlib.pyplot as plt


def plot_output(x, N, angle=False, profile=False):
    """
    Evaluating field stregth E and it intensity IN.
    Plot diffractive element and it distribution of
    diffractive field

    :param x: amplitude matrix
    :param N: resolution of matrix
    :param angle: show phase component
    :param profile: show phase profile
    :return: plots of diffraction element,
    distribution of diffractive field, phase profile
    """
    E = np.fft.fftshift(np.fft.fft2(x))
    IN = (abs(E)/(N*N) * abs(E)/(N*N))
    plt.figure(figsize=(6, 6))
    if angle:
        plt.imshow(np.angle(x), cmap='gray')
    else:
        plt.imshow(x, cmap='gray')
    plt.figure(figsize=(6, 6))
    plt.imshow(IN, cmap='gray')

    if profile:
        # Plot phase profile
        plt.figure(figsize=(6, 6))
        plt.plot(np.angle(x[:, int(N / 2)]))
        plt.xlabel('Profile pixels')
        plt.ylabel('Phase (radiance)')
    plt.show()