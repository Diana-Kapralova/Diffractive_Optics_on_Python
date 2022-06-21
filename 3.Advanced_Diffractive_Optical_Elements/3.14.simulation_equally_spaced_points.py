# This program calculates the phase over a grid
# loads uniformly spaced x and y coordinates
# calculates coefficients using Matlab fit
import scipy.io
import numpy as np

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

    (coefficients, residuals, rank, sing_vals) = np.linalg.lstsq(arg_arr, z, rcond=None)
    return coefficients, residuals, rank, sing_vals


coef, _, _, _ = polynom3d(xh1, yh1, psi1, 5)
