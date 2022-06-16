import numpy as np

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

xh = np.flipud(np.conjugate(xh))
yh = np.flipud(np.conjugate(yh))
print('kk')