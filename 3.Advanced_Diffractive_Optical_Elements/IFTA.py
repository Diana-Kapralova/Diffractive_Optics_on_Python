import numpy as np
from utils import plot_output
import matplotlib.pyplot as plt
import cv2

# CAUTION: image should be with really thin lines
# and part of black area should be greater than wight
# Loading the target image
N = 500
# Read and converting to its binary form
target = cv2.imread('squirrel.jpg', 2)
# Resize img to matrix shape
target = cv2.resize(target, (N, N))
# inverse image where black less than white
target = cv2.bitwise_not(target)
cv2.imwrite("IMAGE_NAME.png", target)

target = target.astype(float)  # Convert symbolic object to a numeric object
# Normalize matrix
target = target/np.max(target)

# Defining DOE phase
DOE = 2*np.pi*np.random.rand(N, N)  # Generate a N x N matrix of random phase between 0 and 2p
s = 1000

# IFTA algorithm
for t in range(s):
    DOEphase = np.exp(1j * DOE)
    # forward iteration
    iterf = np.fft.fft2(DOEphase)
    intf = abs(iterf)
    angf = np.angle(iterf)
    A = target * np.exp(1j * angf)
    # backward iteration
    iterb = np.fft.ifft2(A)
    angb = np.angle(iterb)
    DOE = angb
    error = target - intf/np.max(intf)
    E = np.sum(abs(error))/(N*N)
    if E < 0.05:
        iteration = t
        break
print(E)

plot_output(A, N, angle=True)

