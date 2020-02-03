
import numpy as np
import pandas as pd


# Returns array -> x1 x2 y1 y2 is_checked? gi gj (g:groups) and Summary [group_id, n_elements, diff_y, diff_x]
def create_groups(json_data_arg, sep_value_arg):
    data_shape_val = json_data_arg.shape
    data_prepros_val = np.zeros(shape=[data_shape_val[0], data_shape_val[1] + 5])

    # data_prepros: 0-3(x,y,z) 4(is checked?) 5(area) 6(ratio) 7(g_i) 8(g_j)

    sep = sep_value_arg / 2
    for i_d in range(len(json_data_arg)):
        data_prepros_val[i_d][0] = json_data_arg[i_d][0] - sep
        data_prepros_val[i_d][1] = json_data_arg[i_d][1] + sep
        data_prepros_val[i_d][2] = json_data_arg[i_d][2] - sep
        data_prepros_val[i_d][3] = json_data_arg[i_d][3] + sep

        data_prepros_val[i_d][4] = 0  # (is checked?) init in False

        # area (x2-x1) * (y2-y1)
        diff_x = abs(data_prepros_val[i_d][1] - data_prepros_val[i_d][0])
        diff_y = abs(data_prepros_val[i_d][3] - data_prepros_val[i_d][2])

        area = diff_x * diff_y

        # ratio (x2-x1) / (y2-y1)
        ratio = diff_x / diff_y

        data_prepros_val[i_d][5] = np.round(area, decimals=4)  # area
        data_prepros_val[i_d][6] = np.round(ratio, decimals=4)  # ratio

    #   Init groups
    data_prepros_pd = pd.DataFrame(data_prepros_val)
    data_prepros_pd.sort_values(by=5)
    data_groups = data_prepros_pd.groupby(by=5)

    gi_counter = 0
    summary_val = []
    for g in data_groups:
        # print('-> ' + str(g[0]))
        g_data = g[1]
        g_data_groups = g_data.groupby(by=6)
        for g_d in g_data_groups:
            # print('----> ' + str(g_d[0]))
            # print('--------------> ' + str(gi_counter))
            g_data_data = g_d[1]

            indexes = np.array(g_data_data.index)
            data_prepros_val[indexes, 7] = gi_counter
            data_prepros_val[indexes, 8] = list(range(len(indexes)))

            diff_x = abs(data_prepros_val[indexes[0], 1] - data_prepros_val[indexes[0], 0])
            diff_y = abs(data_prepros_val[indexes[0], 3] - data_prepros_val[indexes[0], 2])

            summary_val.append([gi_counter, len(indexes), diff_y, diff_x])

            gi_counter = gi_counter + 1

    result_data = data_prepros_val[:, [0, 1, 2, 3, 4, 7, 8]]
    return result_data, summary_val
