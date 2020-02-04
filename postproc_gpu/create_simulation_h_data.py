
##
# Create simulation data from adaptive boxes results
##

import numpy as np

from adabox.tools import load_from_json
from postproc_gpu.tools import create_groups, get_xy_units
import matplotlib.colors as colors
import matplotlib.pyplot as plt


colors_list = list(colors._colors_full_map.values())
# plt.ioff()


in_path = "/Users/Juan/django_projects/adaptive-boxes/results/complex.json"      # .json
out_path = "/Users/Juan/django_projects/adaptive-boxes/postproc/h_data/complex.h"    # .jpg


json_data_raw = load_from_json(in_path)

json_data = np.array(json_data_raw['data'])
sep_value = float(json_data_raw['sep_value'])


# data prepros adds boundaries to json rectangles
data_prepros, summary = create_groups(json_data, sep_value)

for s in summary:
    print(s)


n_split_sep_value = 3
error_val = 0.05
y_units, x_units = get_xy_units(data_prepros, sep_value, n_split_sep_value, error_val)


# Print units
for x_unit in x_units:
    print(str(x_unit.group) + ' ' + str(x_unit.position))


for y_unit in y_units:
    print(str(y_unit.group) + ' ' + str(y_unit.position))


# Plot Rectangles by groups
plt.figure()
for rec in data_prepros:
    x1 = rec[0]
    x2 = rec[1]
    y1 = rec[2]
    y2 = rec[3]

    p1 = np.array([x1, y1])
    p2 = np.array([x1, y2])
    p3 = np.array([x2, y1])
    p4 = np.array([x2, y2])

    ps = np.array([p1, p2, p4, p3, p1])
    plt.plot(ps[:, 0], ps[:, 1])


# Save in a csv file








# Save in a h file (C++)
#
#
# data_m = data_matrix.shape[0]
# data_n = data_matrix.shape[1]
#
# np.array_str(data_matrix.flatten())
#
# text_file = open(out_path, "w")
# text_file.write('long m = %d; \nlong n = %d; \n\n' % (data_m, data_n))
# text_file.write('int data[%ld] = { \n' % (data_m*data_n))
#
#
# for i in range(data_m):
#     for j in range(data_n):
#         text_file.write('%d, ' % data_matrix[i][j])
#     text_file.write('\n')
#
#
# text_file.write('};\n\n')
# text_file.close()
#
# print("Work Finished!!")







