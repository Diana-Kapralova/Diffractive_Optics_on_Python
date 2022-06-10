import numpy as np
from utils import plot_output

# # Defining Grating Parameters
N = 500
# A1 = np.zeros((N, N))
# A2 = np.zeros((N, N))
# A = np.zeros((N, N))
# # Define the periods of the gratings
# Px = 100
# Py = 100
# # Define fill factors
FFx = 0.5
# FFy = 0.5
# # Constracting the grating
# for p in range(N-1, 1, -1):
#     for q in range(1, N):
#         if np.remainder(q, Px) < Px*FFx:
#             A1[p, q] = 1
#         if np.remainder(p, Py) < Py*FFy:
#             A2[p, q] = 1
#
# A = np.exp(1j*np.pi*np.logical_xor(A1, A2))

arr = np.array((N, N))
# def triangle(n):
n = 12
arr1 = np.zeros((n, n))
for i in range(0, n):
    for j in range(0, n):
        if (i + j) >= n-1:
            arr1[i][j] = 1
        # arr1[n-i-1][n-j-1] = 0
        # arr1[i][j] = 1
print(arr1)
        # print('0' * (n - i) + '1' * i)

# triangle(6)