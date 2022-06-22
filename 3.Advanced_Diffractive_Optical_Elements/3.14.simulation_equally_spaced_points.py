# This program calculates the phase over a grid
# loads uniformly spaced x and y coordinates
# calculates coefficients using Matlab fit
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import hsv_to_rgb

# value from phase circle
phase_circle_dict = scipy.io.loadmat('phase_circle.mat')
XH1 = phase_circle_dict['XH1']
YH1 = phase_circle_dict['YH1']
sigma = phase_circle_dict['sigma']
k = phase_circle_dict['k']
f = phase_circle_dict['f']
lamb = phase_circle_dict['lambda']
xh1 = phase_circle_dict['xh1']
yh1 = phase_circle_dict['yh1']
psi1 = phase_circle_dict['psi1']


def polynom3d(x, y, z, degree):
    if len(x.shape) == 1:
        x = x.reshape((x.shape[0], 1))
    if len(y.shape) == 1:
        y = y.reshape((y.shape[0], 1))
    # create polynom of degree-th degree
    count = 0
    order_coef = {}
    for i in range(degree + 1):
        for j in range(degree + 1):
            if (i + j) <= degree:

                if i == 0 and j == 0:
                    start_multi = (x**i) * (y**j)
                    # print(start_multi)
                else:
                    multi = (x ** i) * (y ** j)
                    arg_arr = np.hstack((start_multi, multi))
                    start_multi = arg_arr
                order = (i, j)
                order_coef[order] = count
                count += 1

    print(count)
    (coefficients, residuals, rank, sing_vals) = np.linalg.lstsq(arg_arr, z, rcond=None)

    coef_dict = {}
    # create dict - power of polynom's member: coefficient near this member
    for key, value in order_coef.items():
        coef_dict[key] = coefficients[value]

    return coef_dict, residuals, rank, sing_vals


coef_dict, _, _, _ = polynom3d(xh1, yh1, psi1, 5)

psi_result = 0

for i, j in coef_dict.keys():
    z = coef_dict[(i, j)]
    psi_result += coef_dict[(i, j)] * XH1 ** i * YH1 ** j

# Output
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(XH1, YH1, psi_result, cmap=cm.inferno)
plt.title('Phase over DOE')

# To simulate output intensity
gaus_beam = np.exp(-(XH1**2 + YH1**2)/sigma**2)  # Gaussian beam
amp1 = np.exp(1j * psi_result) * gaus_beam  # Amplitude just after hologram
# amp1 in this situation not have NANs if it has we should replace it by 0
amp1 = amp1 * np.exp(1j*(k/(2*f)) * (XH1**2 + YH1**2))


# function for image complex array
def complex2hsv(complex_arr, hue_start=90):
    amp = np.abs(complex_arr)
    ph = np.angle(complex_arr, deg=True) + hue_start
    # HSV are values in range [0,1]
    h = (ph % 360) / 360
    s = 0.85 * np.ones_like(h)
    v = amp/np.max(amp)
    return hsv_to_rgb(np.dstack((h, s, v)))


im = complex2hsv(amp1 * np.conjugate(amp1))

plt.figure(figsize=(8, 8))
plt.imshow(im)
plt.contour(XH1, YH1, amp1 * np.conjugate(amp1))
plt.title('Intensity just after DOE')
plt.xlabel('X-direction')
plt.ylabel('Y-direction')

amp2 = np.fft.fftshift(np.fft.fft2(amp1))

plt.figure(figsize=(8, 8))
plt.contour(abs(amp2)/np.max(amp2))
plt.title('Output intensity - Gaussian to square')
plt.xlabel('X-direction')
plt.ylabel('Y-direction')
plt.show()