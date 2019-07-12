
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool


def get_right_bottom_rectangle(idx_i_arg, idx_j_arg, n_arg, m_arg):
    step_j = 0
    first_step_i = 0

    while True:
        i = idx_i_arg
        j = idx_j_arg + step_j

        if j == n_arg:
            break

        temp_val = data_matrix[i, j]
        if temp_val == 0:
            break

        step_i = 0
        while True:
            i = idx_i_arg + step_i

            if i == m_arg:
                break

            temp_val = data_matrix[i, j]

            if temp_val == 0:
                break

            step_i += 1

        if step_j == 0:
            first_step_i = step_i
        else:
            if step_i < first_step_i:
                break

        step_j += 1

    x1_val = idx_j_arg
    y1_val = idx_i_arg
    x2_val = idx_j_arg + step_j - 1
    y2_val = idx_i_arg + first_step_i - 1

    return x1_val, x2_val, y1_val, y2_val


def get_left_bottom_rectangle(idx_i_arg, idx_j_arg, m_arg):
    step_j = 0
    first_step_i = 0

    while True:
        i = idx_i_arg
        j = idx_j_arg - step_j

        if j == 0:
            break

        temp_val = data_matrix[i, j]
        if temp_val == 0:
            break

        step_i = 0
        while True:
            i = idx_i_arg + step_i

            if i == m_arg:
                break

            temp_val = data_matrix[i, j]

            if temp_val == 0:
                break

            step_i += 1

        if step_j == 0:
            first_step_i = step_i
        else:
            if step_i < first_step_i:
                break

        step_j += 1

    x1_val = idx_j_arg
    y1_val = idx_i_arg
    x2_val = idx_j_arg - step_j + 1
    y2_val = idx_i_arg + first_step_i - 1

    return x1_val, x2_val, y1_val, y2_val


def get_left_top_rectangle(idx_i_arg, idx_j_arg):
    step_j = 0
    first_step_i = 0

    while True:
        i = idx_i_arg
        j = idx_j_arg - step_j

        if j == 0:
            break

        temp_val = data_matrix[i, j]
        if temp_val == 0:
            break

        step_i = 0
        while True:
            i = idx_i_arg - step_i

            if i == -1:
                break

            temp_val = data_matrix[i, j]

            if temp_val == 0:
                break

            step_i += 1

        if step_j == 0:
            first_step_i = step_i
        else:
            if step_i < first_step_i:
                break

        step_j += 1

    x1_val = idx_j_arg
    y1_val = idx_i_arg
    x2_val = idx_j_arg - step_j + 1
    y2_val = idx_i_arg - first_step_i + 1

    return x1_val, x2_val, y1_val, y2_val


def get_right_top_rectangle(idx_i_arg, idx_j_arg, n_arg):
    step_j = 0
    first_step_i = 0

    while True:
        i = idx_i_arg
        j = idx_j_arg + step_j

        if j == n_arg:
            break

        temp_val = data_matrix[i, j]
        if temp_val == 0:
            break

        step_i = 0
        while True:
            i = idx_i_arg - step_i

            if i == -1:
                break

            temp_val = data_matrix[i, j]

            if temp_val == 0:
                break

            step_i += 1

        if step_j == 0:
            first_step_i = step_i
        else:
            if step_i < first_step_i:
                break

        step_j += 1

    x1_val = idx_j_arg
    y1_val = idx_i_arg
    x2_val = idx_j_arg + step_j - 1
    y2_val = idx_i_arg - first_step_i + 1

    return x1_val, x2_val, y1_val, y2_val



in_path = '/Users/Juan/django_projects/adaptive-boxes/data_prepros/complex.binary'
out_path = ''

data_matrix = np.loadtxt(in_path, delimiter=",")

# Flatten Matrix
data_matrix_f = data_matrix.flatten()

# Kernel Data

dim3_block_x = 1
dim3_block_y = 1

block_dim_y = 1
block_dim_x = 1

# KERNEL
# Kernel non-editable - they go in for-loop
block_idx_x = 0
block_idx_y = 0

thread_idx_x = 0
thread_idx_y = 0

# Kernel editable
# Params
#       4 threads: [right-bottom right_top , left-bt, left-tp], 4 coords: [x1 x2 y1 y2]
coords = np.zeros(shape=[4, 4])    # Could be stored in Cache- Shared Memory
idx_i = 1   # y rand point
idx_j = 1   # x rand point



# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.imshow(data_matrix)
ax.set_aspect('equal')

n = data_matrix.shape[1]    # for j
m = data_matrix.shape[0]    # for i


stop_flag = False
counter = 0
while not stop_flag:

    counter += 1

    if counter > 2:
        stop_flag = True

    (data_matrix == 1).sum()

    ones_counter = (data_matrix == 1).sum()
    print(ones_counter)
    if ones_counter == 0:
        stop_flag = True

    search_end_flag = False
    while not search_end_flag:
        idx_i = int(np.random.rand()*m)   # y rand point
        idx_j = int(np.random.rand()*n)   # x rand point
        if data_matrix[idx_i, idx_j] == 1:
            search_end_flag = True

    # idx_i = 19
    # idx_j = 125

    # plt.scatter(idx_j, idx_i, c='r')

    x1, x2, y1, y2 = get_right_bottom_rectangle(idx_i, idx_j, n, m)
    coords[0, :] = np.array([x1, x2, y1, y2])

    x1, x2, y1, y2 = get_right_top_rectangle(idx_i, idx_j, n)
    coords[1, :] = np.array([x1, x2, y1, y2])

    x1, x2, y1, y2 = get_left_bottom_rectangle(idx_i, idx_j, m)
    coords[2, :] = np.array([x1, x2, y1, y2])

    x1, x2, y1, y2 = get_left_top_rectangle(idx_i, idx_j)
    coords[3, :] = np.array([x1, x2, y1, y2])


    # coords[]
    pr = coords[[0, 1], 1].min()
    pl = coords[[2, 3], 1].max()

    pb = coords[[0, 2], 3].min()
    pt = coords[[1, 3], 3].max()

    # final x1x2 and y1y2
    x1 = int(pl)
    x2 = int(pr)
    y1 = int(pb)
    y2 = int(pt)

    plt.scatter(x1, y1, c='r')
    plt.scatter(x2, y2, c='b')

    p1 = np.array([x1, y1])
    p2 = np.array([x1, y2])
    p3 = np.array([x2, y1])
    p4 = np.array([x2, y2])
    ps = np.array([p1, p2, p4, p3, p1])
    plt.plot(ps[:, 0], ps[:, 1], c='r')

    # write data
    data_matrix[y2:y1, x1:x2] = 0


# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.imshow(data_matrix)
ax.set_aspect('equal')
