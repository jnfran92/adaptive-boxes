
from adabox import proc
from adabox.plot_tools import plot_rectangles, plot_rectangles_only_lines
import numpy as np
import matplotlib.pyplot as plt

# Input Path
in_path = './sample_data/humboldt_binary_matrix.csv'

# Load Demo data with columns [x_position y_position flag]
data_2d = np.loadtxt(in_path, delimiter=",")


# Plot demo data
plt.scatter(data_2d[:, 0], data_2d[:, 1])
plt.axis('scaled')

