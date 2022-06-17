import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# program creates a mesh of zones of equal energy
# for a Gaussian beam
# mesh is rotated away from axes to avoid zeros

sigma = 0.8  # Gaussian spot size
R = 1 #  radius of beam
# mesh coordinates
I = 20  # related to rows and therefore also to y coords
J = 20  # related to columns and therefore also to x coords
N = (I * J)  # total number of zones
TP = np.pi * sigma**2/2  # total power
P = (1 - np.exp(-2 * R**2/sigma**2)) * TP  # total power in radius R
rings = int(I/2)
P_ring = P/rings  # power per ring

# calculating radii of rings
n = np.array([i for i in range(rings)])
r = sigma * np.sqrt((0.5 * np.log(1/(1 - (n+1) * P_ring))))

# add very small value for first ring (close to zero)
rad = np.zeros(len(n) + 1)
rad[0] = 1e-10
for i in n:
    rad[i + 1] = r[i]
r = rad

# number of zones in a ring-decided by angles chosen
angle_step = np.pi/I
angle_shift = np.pi/100

count1 = 0
for theta in np.arange((np.pi - angle_shift), -2*angle_shift, -angle_step):
    count1 += 1
    if theta == (np.pi - angle_shift):
        xh = r * np.cos(theta)
        yh = r * np.sin(theta)
    else:
        xh_temp = r * np.cos(theta)
        xh = np.vstack([xh, xh_temp])
        yh_temp = r * np.sin(theta)
        yh = np.vstack([yh, yh_temp])

xh = np.flipud(np.transpose(xh))
yh = np.flipud(np.transpose(yh))
theta = (np.pi-angle_shift) + angle_step

for count2 in range(count1):
    if theta == ((np.pi - angle_shift) + angle_step):
        xh1 = r * np.cos(theta)
        yh1 = r * np.sin(theta)
    else:
        xh1_temp = r * np.cos(theta)
        xh1 = np.vstack([xh1, xh1_temp])
        yh1_temp = r * np.sin(theta)
        yh1 = np.vstack([yh1, yh1_temp])
    theta = theta + angle_step

xh1 = np.transpose(xh1)
yh1 = np.transpose(yh1)
xh = np.vstack([xh[0:-1, :], xh1])
yh = np.vstack([yh[0:-1, :], yh1])

plt.figure(figsize=(6, 6))
plt.plot(xh, yh, 'k.')
plt.title('Locations of nodes of a Gaussian input')
plt.xlabel('X-direction (arb. units)')
plt.ylabel('Y-direction (arb. units)')

plt.figure(figsize=(6, 6))
plt.plot(np.transpose(xh), np.transpose(yh))
plt.title('Annular rings of a Gaussian input')
plt.xlabel('X-direction (arb. units)')
plt.ylabel('Y-direction (arb. units)')
plt.show()

val_dict = {'I': I, 'J': J, 'R': R, 'sigma': sigma,
            'xh': xh, 'yh': yh}

scipy.io.savemat('GaussianMesh.mat', val_dict)
dic = scipy.io.loadmat('GaussianMesh.mat', val_dict)
