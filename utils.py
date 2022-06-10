import numpy as np
import matplotlib.pyplot as plt

def plot_output(x, N, angle=False):
    """
    Evaluating field stregth E and it intensity IN.
    Plot diffractive element and it distribution of
    diffractive field

    :param x: amplitude matrix
    :param N: resolution of matrix
    :param angle: show phase component
    :return: plots of diffraction element
    and distribution of diffractive field
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
    plt.show()