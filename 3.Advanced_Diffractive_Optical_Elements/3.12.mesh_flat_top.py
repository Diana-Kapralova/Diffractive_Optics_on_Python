import matplotlib.pyplot as plt
import numpy as np
import scipy.io

# I, J will be available in GaussianMesh.mat
val_dict = scipy.io.loadmat('GaussianMesh.mat')
I = int(val_dict['I'])
J = int(val_dict['J'])

S = 2  # size of square at image plane is 2S
step_x = 2*S/J
step_y = 2*S/I
X = np.array([a for a in np.arange(-S, S + step_x, step_x)])
Y = np.array([b for b in np.arange(-S, S + step_y, step_y)])
xsq, ysq = np.meshgrid(X, Y)
xsq = np.flipud(xsq)
ysq = np.flipud(ysq)
plt.figure(figsize=(6, 6))
plt.plot(xsq, ysq, 'b.')
plt.xlabel('X-direction (arb. units)')
plt.ylabel('Y-direction (arb. units)')
plt.show()

bits = 512
step_x = 2 * S/bits
step_y = 2 * S/bits
# regular spaced points
index_x = np.array([a for a in np.arange(-S, S + step_x, step_x)])
# even number of points
index_x = index_x[:-1]
# regular spaced points
index_y = np.array([b for b in np.arange(-S, S + step_y, step_y)])
# even number of points
index_y = index_y[:-1]
# creates grid of points with limits given by index
XS, YS = np.meshgrid(index_x, index_y)
# Saves mesh details and variables in a file called
# square for use by further programs
val_dict = {'xsq': xsq, 'ysq': ysq, 'XS': XS, 'YS': YS}

scipy.io.savemat('square.mat', val_dict)


