import numpy as np
from utils import plot_output
import matplotlib.pyplot as plt
import cv2

# CAUTION: image should be with really thin lines
# and part of black area should be greater than wight
# Loading the target image
N = 500
# Read and converting to its binary form
target = cv2.imread('/home/diakap/DATA/Diffract_Optics/Diffractive_Optics_on_Python/3.Advanced_Diffractive_Optical_Elements/butterfly_3.jpg', 2)
# Resize img to matrix shape
target = cv2.resize(target, (N, N))
th, target = cv2.threshold(target, 128, 255, cv2.THRESH_BINARY)
# inverse image where black less than white
target = 255 - target
cv2.imwrite("IMAGE_NAME.png", target)

target = target.astype(float)  # Convert symbolic object to a numeric object
# Normalize matrix
target = target/np.max(target)

# Defining DOE phase
DOE = 2*np.pi*np.random.rand(N, N)  # Generate a N x N matrix of random phase between 0 and 2p
s = 100

# three-level part
DOE1 = np.zeros((N, N))
g = 3  # Define the number of phase levels
delphase = 2 * np.pi/g
for p in range(N):
    # phase profile
    for q in range(N):
        for n in range(g):
            if (- np.pi + n * delphase) < DOE[p, q] <= (-np.pi + (n + 1) * delphase):
                DOE1[p, q] = n * delphase

# IFTA algorithm
for t in range(s):
    DOEphase = np.exp(1j * DOE1)
    # forward iteration
    iterf = np.fft.fft2(DOEphase)
    intf = abs(iterf)
    angf = np.angle(iterf)
    A = target * np.exp(1j * angf)
    # backward iteration
    iterb = np.fft.ifft2(A)
    angb = np.angle(iterb)
    DOE1 = angb
    error = target - intf/np.max(intf)
    E = np.sum(abs(error))/(N*N)
    if E < 0.05:
        iteration = t
        break

plot_output(A, N, angle=True)