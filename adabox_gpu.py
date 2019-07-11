
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



# Plot
fig = plt.figure(figsize=(6, 3.2))
ax = fig.add_subplot(111)
plt.imshow(data_matrix)
ax.set_aspect('equal')


# Flatten Matrix
data_matrix_f = data_matrix.flatten()

# Kernel Data

dim3_block_x = data_matrix.shape[1]
dim3_block_y = data_matrix.shape[0]

block_dim_y = dim3_block_y
block_dim_x = dim3_block_x

# KERNEL
# Kernel non-editable - they go in for-loop
block_idx_x = 0
block_idx_y = 0

thread_idx_x = 0
thread_idx_y = 0

# Kernel editable
# Params
distances = np.zeros(shape=[data_matrix_f.shape[0]])    # Could be stored in Cache- Shared Memory
idx_i = 0   # y rand point
idx_j = 1   # x rand point

plt.scatter(idx_j, idx_i, c='r')

# Run Kernel
for thread_idx_y in range(block_dim_y):
    for thread_idx_x in range(block_dim_x):
        # print('running threadId.x: ' + str(thread_idx_x) + ' threadId.y: ' + str(thread_idx_y))
        i = thread_idx_y
        j = thread_idx_x

        g_i = block_dim_y * block_idx_y + i
        g_j = block_dim_x * block_idx_x + j

        m = block_dim_y
        n = block_dim_x

        plt.scatter(j, i, c='b', marker='x')

        val_in_b = data_matrix_f[n * i + j]
        val_in_a = data_matrix_f[n * i + idx_j]

        distance_j = (j - idx_j) * val_in_b * val_in_a
        distance_i = (i - idx_i) * val_in_b * val_in_a
        print('i: ' + str(i) + '  j: ' + str(j) + '   distance  ' + str(distance_j))

        if distance_j > 0:
            distances[i * n + j] = abs(distance_j) + abs(distance_i)

print(distances.reshape([m, n]))


# Break
# Get min distance in left - Atomic can be used(In this case: min() function)
for thread_idx_y in range(block_dim_y):
    for thread_idx_x in range(block_dim_x):
        # print('running threadId.x: ' + str(thread_idx_x) + ' threadId.y: ' + str(thread_idx_y))
        i = thread_idx_y
        j = thread_idx_x

        g_i = block_dim_y * block_idx_y + i
        g_j = block_dim_x * block_idx_x + j

        m = block_dim_y
        n = block_dim_x

        if(j == 0):
            distances[i*n + 0: i*n + m]



