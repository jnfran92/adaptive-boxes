
import ctypes
# from ctypes import *
from adabox import proc
from adabox.plot_tools import plot_rectangles, plot_rectangles_only_lines
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from adabox.tools import load_from_json, Rectangle, save_to_json

so_file = "/Users/kolibri/PycharmProjects/adaptive-boxes/adabox/decomposition/cpp/getters.so"
getters = ctypes.CDLL(so_file)


# Input Path
in_path = './sample_data/squares.csv'

# Load Demo data with columns [x_position y_position flag]
data_matrix = np.loadtxt(in_path, delimiter=",")
data_matrix = data_matrix.astype(np.intc)

# Plot demo data
plt.imshow(np.flip(data_matrix, axis=0), cmap='magma', interpolation='nearest')

idx = 7
idj = 12

m = data_matrix.shape[0]
n = data_matrix.shape[1]
#
# results1 = np.array([0, 0, 0, 0]).astype(np.intc)
# results2 = np.array([0, 0, 0, 0]).astype(np.intc)
# results3 = np.array([0, 0, 0, 0]).astype(np.intc)
# results4 = np.array([0, 0, 0, 0]).astype(np.intc)
#
# c_int_p = ctypes.POINTER(ctypes.c_int)
# data_matrix_ptr = data_matrix.ctypes.data_as(c_int_p)
#
# results1_ptr = results1.ctypes.data_as(c_int_p)
# results2_ptr = results2.ctypes.data_as(c_int_p)
# results3_ptr = results3.ctypes.data_as(c_int_p)
# results4_ptr = results4.ctypes.data_as(c_int_p)
#
# getters.get_right_bottom_rectangle(idx, idj, m, n, data_matrix_ptr, results1_ptr)
# getters.get_left_bottom_rectangle(idx, idj, m, n, data_matrix_ptr, results2_ptr)
#
# getters.get_right_top_rectangle(idx, idj, n, data_matrix_ptr, results3_ptr)
# getters.get_left_top_rectangle(idx, idj, n, data_matrix_ptr, results4_ptr)

out = np.array([0, 0, 0, 0]).astype(np.intc)

c_int_p = ctypes.POINTER(ctypes.c_int)

data_matrix_ptr = data_matrix.ctypes.data_as(c_int_p)
out_ptr = out.ctypes.data_as(c_int_p)
getters.find_largest_rectangle(idx, idj, m, n, data_matrix_ptr, out_ptr)


def plot_rectangles_only_lines(recs_arg, sep_value_arg):
    max_area_val = np.max([item.get_area() for item in recs_arg])

    # fig = plt.figure()
    # plt.axis('off')
    # ax = fig.add_subplot(111)

    sep_to_plot = sep_value_arg / 2
    for rec_val in recs_arg:
        plot_rectangle_lines(rec_val, sep_to_plot, max_area_val, ax)

    # plt.axis('scaled')
    # fig.tight_layout()


def plot_rectangle_lines(rec_arg: Rectangle, sep_to_plot_arg, max_area_arg, ax):
    p1 = np.array([rec_arg.x1 - sep_to_plot_arg, rec_arg.y1 - sep_to_plot_arg])
    p2 = np.array([rec_arg.x1 - sep_to_plot_arg, rec_arg.y2 + sep_to_plot_arg])
    p3 = np.array([rec_arg.x2 + sep_to_plot_arg, rec_arg.y1 - sep_to_plot_arg])
    p4 = np.array([rec_arg.x2 + sep_to_plot_arg, rec_arg.y2 + sep_to_plot_arg])

    ps = np.array([p1, p2, p4, p3, p1])

    max_n = 300
    max_log = np.log2(max_n + 1)
    area_ratio = (max_n*(rec_arg.get_area()/max_area_arg))+1
    line_w = np.log2(area_ratio)/max_log
    # plt.plot(ps[:, 0], ps[:, 1], linewidth=0.1*line_w + 0.05, c='red')
    max_n = 300
    max_log = np.log2(max_n + 1)
    area_ratio = (max_n*(rec_arg.get_area()/max_area_arg))+1
    line_w = np.log2(area_ratio)/max_log
    # plt.plot(ps[:, 0], ps[:, 1], linewidth=0.1*line_w + 0.05, c='red')
    plt.plot(ps[:, 0], ps[:, 1], linewidth=0.05, c='red')

    rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color='yellow', lw=0)
    # rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color=next(cycol), lw=0)
    # rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color=np.random.rand(3,), lw=0)
    ax.add_patch(rect)

    plt.plot(ps[:, 0], ps[:, 1], linewidth=0.05, c='red')

    rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color='yellow', lw=0)
    # rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color=next(cycol), lw=0)
    # rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color=np.random.rand(3,), lw=0)
    ax.add_patch(rect)


results = [out]
recs = list(map(lambda rec: Rectangle(rec[0], rec[1], rec[2], rec[3]), results))


# Plot demo data
fig = plt.figure()
plt.axis('off')
ax = fig.add_subplot(111)
# plt.imshow(np.flip(data_matrix, axis=0), cmap='magma', interpolation='nearest')
plt.imshow(data_matrix, cmap='magma', interpolation='nearest')
plot_rectangles_only_lines(recs, 1)

coords = np.argwhere(data_matrix == 1)
plt.scatter(coords[:, 1], coords[:, 0])
plt.show()
