
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

# if len(sys.argv) < 3:
#     print('ERROR Args number. Needed: \n[1]In Path(with file.npy) -- prepros file \n[2]Out Path(with .json)')
#     sys.exit()
#
#
# in_path = str(sys.argv[1])
# out_path = str(sys.argv[2])


in_path = '/Users/Juan/django_projects/adaptive-boxes/data_prepros/squares.binary'
out_path = ''

data_matrix = np.loadtxt(in_path, delimiter=",")


# Plot
fig = plt.figure(figsize=(6, 3.2))
ax = fig.add_subplot(111)
plt.imshow(data_matrix)
ax.set_aspect('equal')


# init
a = data_matrix[0, :]
b = data_matrix[1, :]



matmul = data_matrix.dot(data_matrix.T)


# Plot
fig = plt.figure(figsize=(6, 3.2))
ax = fig.add_subplot(111)
plt.imshow(matmul)
ax.set_aspect('equal')


a = np.array([[1, 0, 1],
              [1, 1, 1],
              [1, 1, 1],
              ])

b = np.array([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 0],
              ])

r = a.dot(b)


# Flatten Matrix
data_matrix_f = data_matrix.flatten()

# Kernel Data

dim3_block_x = data_matrix.shape[0]
dim3_block_y = data_matrix.shape[1]

block_dim_y = dim3_block_y
block_dim_x = dim3_block_x


# KERNEL
# Kernel non-editable - they go in for-loop
block_idx_x = 0
block_idx_y = 0

thread_idx_x = 0
thread_idx_y = 0

# Kernel editable
i = thread_idx_y
j = thread_idx_x

g_i = block_dim_y * block_idx_y + i
g_j = block_dim_x * block_dim_x + j

m = block_dim_y
n = block_dim_x

idx_i = 0
idx_j = 1

mat_val = data_matrix_f[m*i + j]

distance_j = abs(g_j - j)


# if mat_val == 0:
#     if idx_j > j_g:
#         print('idx_j is at left')
#     else:
#         print('idx_j is at right')



