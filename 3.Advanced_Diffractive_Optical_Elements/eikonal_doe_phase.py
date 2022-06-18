import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.io
import pickle

'''
1. This program reads mesh data from the files GaussianMesh and square
2. Phase over the hologram is calculated using the Eikonal technique
3. Phase is calculated at a limited number of irregularly spaced data points
'''
value_gaus = scipy.io.loadmat('GaussianMesh.mat')
value_square = scipy.io.loadmat('square.mat')

# inputs
f = 300  # distance between input and output planes in mm
lamb = 0.000633  # wavelength in mm

bits = 512
x = value_square['xsq']
y = value_square['ysq']
xh = value_gaus['xh']
yh = value_gaus['yh']
J = int(value_gaus['J'])
I = int(value_gaus['I'])
R = int(value_gaus['R'])
sigma = value_gaus['sigma']

plt.figure(figsize=(8, 8))
plt.plot(xh, yh, 'r.')
plt.title('Mesh over hologram plane')

# Eikonal retrieval
# delta psi
delta_psi_x = (x - xh) / f
delta_psi_y = (y - yh) / f

# polinomial calculation to obtain phase of hologram
D = 5  # polinomial of degree D
M = (D + 2) * (D + 1) / 2

# calculates k and l values for each m value
count = 0
indices_list = []
for k in range(D + 1):
    for l in range(D + 1 - k):
        m = k * ((2 * D - k + 3) / 2) + l + 1
        indices_list.append([m, k, l])
        count += 1
indices = np.array(indices_list)

c = np.zeros((int(M) - 1, int(M) - 1))
b = np.zeros((int(M) - 1, 1))
for n in np.arange(1, int(M)):
    for m in np.arange(1, int(M)):
        m1 = m - 1
        n1 = n - 1
        c[n1, m1] = 0
        b[n1, 0] = 0
        for j1 in range(J + 1):
            for i1 in range(I + 1):
                k = indices[m, 1]
                k1 = indices[n, 1]
                l = indices[m, 2]
                l1 = indices[n, 2]
                c[n1, m1] = c[n1, m1] + (k * k1 * (xh[j1, i1] ** (k + k1 - 2)) * (yh[j1, i1] ** (l + l1))) + \
                            (l * l1*(xh[j1, i1] ** (k + k1)) * (yh[j1, i1] ** (l + l1 - 2)))
                b[n1, 0] = b[n1, 0] + delta_psi_x[j1, i1]*k1*(xh[j1, i1]**(k1 - 1))*(yh[j1, i1]**l1) + \
                           delta_psi_y[j1, i1]*l1*(xh[j1, i1]**k1)*(yh[j1, i1]**(l1 - 1))

# coefficients
a = np.linalg.solve(c, b)

del delta_psi_y, delta_psi_x
# eikonal - psi
psi = np.zeros((J + 1, I + 1))
for j1 in range(J + 1):
    for i1 in range(I + 1):
        psi[j1, i1] = 0
        for m in range(1, int(M)):
            psi[j1, i1] = psi[j1, i1] + a[m-1]*(xh[j1, i1]**indices[m, 1])*(yh[j1, i1]**indices[m, 2])

del a, b, c

k = 2*np.pi/lamb
psi = k * psi  # phase of hologram

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(xh, yh, psi, cmap=cm.RdYlGn)
plt.title('Phase of hologram')
plt.xlabel('X-cordinate in units of length')
plt.ylabel('Y-cordinate in units of length')
ax.set_zlabel('Phase (radians)')
plt.show()

# save phase psi xh yh
step = R*2/bits
# converting arrays to vectors - required for fit process

m, n = xh.shape
xh1 = xh[:, 0]
yh1 = yh[:, 0]
psi1 = psi[:, 0]
j = xh[:, 1]
# for i in range(1, n):
xh1 = np.reshape(xh, (xh.shape[0]*xh.shape[1], 1), order='F')
yh1 = np.reshape(yh, (yh1.shape[0]*yh.shape[1], 1), order='F')
psi1 = np.reshape(psi, (psi.shape[0]*psi.shape[1], 1), order='F')

# saves data in files that can be retrieved by software that will
# carry out regression
# and generate coefficients to help generate phase at equidistant
# points
value_dict = {'xh1': xh1, 'yh1': yh1, 'psi1': psi1}
f = open('testdata.pkl', 'wb')
pickle.dump(value_dict, f)
f.close()
# -----------------
index = np.arange(-R, R, step)  # regular spaced points
index = index[0:-1]  # even number of points
XH1, YH1 = np.meshgrid(index, index)  # creates grid of points with limits given by index
# store regularly spaced points and phase for later use
value_dict = {'XH1': XH1, 'YH1': YH1, 'sigma': sigma,
              'k': k, 'f': f, 'lambda': lamb, 'xh1': xh1,
              'yh1': yh1, 'psi1': psi1}
scipy.io.savemat('phase_circle.mat', value_dict)





