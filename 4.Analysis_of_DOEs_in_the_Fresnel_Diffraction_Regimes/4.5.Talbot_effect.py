import matplotlib.pyplot as plt
import numpy as np

"""
Talbot effect - When a plane wave illuminates a diffraction grating, 
an image of the grating occurs at periodic distances 
along the optical axis. The effect is visible for both
amplitude and phase diffraction gratings. 
Since the image is a copy of the original grating,
it is also called a self-image.
"""

lamb = 600*10**(-9)  # in meters
k = 2 * np.pi/lamb

# Defining Grating Parameters
N = 2000  # matrix size
P = 75  # period of gratings in pixels
FF = 0.25  # Define fill factor
period = P * 10**(-6)
A = np.ones((1, N))  # Define a matrix by assigning 1 to all pixels


# Constructing the Gratings
q = np.array([k for k in np.arange(1, N+1)])
zk = np.fmod(q, P)
A[:, np.fmod(q, P) < P*FF] = 0
A = np.tile(A, (N, 1))  # replicate the row to create a 2-d grating

# Create a window around the grating of pixel width w
w = 500
A[:w, :] = 0
A[(N-w):N, :] = 0
A[:, :w] = 0
A[:, (N-w):N] = 0

# Talbot distance
zT = (2 * period**2)/lamb  # Talbot distance

# Creating sampled space
r0 = (N/P)*period/2  # radius of input beam
step = 2 * r0/(N - 1)
index = np.arange(-r0, r0 + step/2, step)  # regular spaced points
XH, YH = np.meshgrid(index, index)  # creates grid of points with limits given by index

# run this program at various distances
dist = [zT/4, zT/2, zT]

# plot parameters
nrows = 1
ncols = len(dist)
fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15, 8))
plt.subplots_adjust(hspace=0.33)

for d in dist:
    z0 = d / zT  # distance in terms of Telbot distance
    a = str(z0)  # used to label figures
    # Observing the grating output in the near-field
    E = (A * np.exp((1j * k / (2 * d)) * (XH ** 2 + YH ** 2))) / (lamb * d)
    E = np.fft.fftshift(np.fft.fft2(E))
    I = (abs(E) / (N*N)) * (abs(E)/(N*N))  # Calculating intensity
    ax = axs[dist.index(d)]
    ax.imshow(I, cmap='gray')
    ax.set_title('Propagation distance ' + str(round(d * 100, 4)) + ' cm')

plt.show()

