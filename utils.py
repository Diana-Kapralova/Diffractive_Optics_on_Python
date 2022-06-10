import numpy as np
import matplotlib.pyplot as plt

def norm_output(x, N):
    """
    Evaluating field stregth E and it intensity IN.
    Plot diffractive element and it distribution of
    diffractive field

    :param x: amplitude matrix
    :param N: resolution of matrix
    :return: plots of diffraction element
    and distribution of diffractive field
    """
    E = np.fft.fftshift(np.fft.fft2(x))
    IN = (abs(E)/(N*N) * abs(E)/(N*N))
    plt.figure(figsize=(6, 6))
    plt.imshow(x, cmap='gray')
    plt.figure(figsize=(6, 6))
    plt.imshow(IN, cmap='gray')
    plt.show()