
import ctypes
# from ctypes import *
from adabox import proc
from adabox.plot_tools import plot_rectangles, plot_rectangles_only_lines
import numpy as np
import matplotlib.pyplot as plt

so_file = "/Users/kolibri/PycharmProjects/adaptive-boxes/adabox/decomposition/cpp/getters.so"
getters = ctypes.CDLL(so_file)


# Input Path
in_path = './sample_data/humboldt_binary_matrix.csv'

# Load Demo data with columns [x_position y_position flag]
data_matrix = np.loadtxt(in_path, delimiter=",")


# Plot demo data
plt.imshow(np.flip(data_matrix, axis=0), cmap='magma', interpolation='nearest')

idx = 0
idj = 0
m = data_matrix.shape[0]
n = data_matrix.shape[1]
results = np.array([0, 0, 0, 0])

data_matrix_ptr = data_matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
results_ptr = results.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
getters.get_right_bottom_rectangle(idx, idj, m, n, data_matrix_ptr, results_ptr)




