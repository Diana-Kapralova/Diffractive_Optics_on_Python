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

# p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2 + p30*x^3 + p21*x^2*y
#                     + p12*x*y^2 + p03*y^3 + p40*x^4 + p31*x^3*y + p22*x^2*y^2
#                     + p13*x*y^3 + p04*y^4 + p50*x^5 + p41*x^4*y + p32*x^3*y^2
#                     + p23*x^2*y^3 + p14*x*y^4 + p05*y^5
xh1 = xh1.flatten()
yh1 = yh1.flatten()
def polynom3d(x, y, z, degree):
    arg_x = np.vander(x, degree)
    arg_y = np.vander(y, degree)
    all_args = np.hstack((arg_x, arg_y))
    (coefficients, residuals, rank, sing_vals) = np.linalg.lstsq(all_args, z)
    return coefficients, residuals, rank, sing_vals

coef, _, _, _ = polynom3d(xh1, yh1, psi1, 5)
print(coef)