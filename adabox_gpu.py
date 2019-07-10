
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


a = np.array([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1],
              ])

r = a.dot(a)

