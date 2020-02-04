
##
# Create simulation data from adaptive boxes results
##

import numpy as np

from adabox.tools import load_from_json
from postproc_gpu.tools import create_groups, get_xy_units
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import pandas as pd


colors_list = list(colors._colors_full_map.values())
# plt.ioff()


in_path = "/Users/Juan/django_projects/adaptive-boxes/postproc_gpu/gpu_csv/squares_gpu.csv"      # .csv
out_path = "/Users/Juan/django_projects/adaptive-boxes/postproc_gpu/csv_out_data"    # .csv


data = np.array(pd.read_csv(in_path, header=None))
sep_value = 1

# data prepros adds boundaries to json rectangles
data_prepros, summary = create_groups(data, sep_value)

for s in summary:
    print(s)


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
n_split_sep_value = 3
error_val = 0.05
y_units, x_units = get_xy_units(data_prepros, sep_value, n_split_sep_value, error_val)


# Creating units
x_unit_list = []
for x_unit in x_units:
    # print(str(x_unit.group) + ' ' + str(x_unit.position))
    x_unit_list.append([x_unit.group[0][0],
                        x_unit.group[0][1],
                        x_unit.position[0],
                        x_unit.group[1][0],
                        x_unit.group[1][1],
                        x_unit.position[1],
                        ])


y_unit_list = []
for y_unit in y_units:
    # print(str(y_unit.group) + ' ' + str(y_unit.position))
    y_unit_list.append([y_unit.group[0][0],
                        y_unit.group[0][1],
                        y_unit.position[0],
                        y_unit.group[1][0],
                        y_unit.group[1][1],
                        y_unit.position[1],
                        ])

# x-units and y-units
# columns: (0: group, 1:partition, 2:interface_position) (3:group, 4:partition, 5:interface_position)
x_unit_df = pd.DataFrame(x_unit_list)
y_unit_df = pd.DataFrame(y_unit_list)

x_unit_df.to_csv(out_path+"/x_units.csv", header=None)
y_unit_df.to_csv(out_path+"/y_units.csv", header=None)





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







