
import sys
from lib.tools import load_from_json, Rectangle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as colors
plt.ioff()


def plot_rectangles(recs_arg, sep_value_arg):
    max_area_val = np.max([item.get_area() for item in recs_arg])

    fig = plt.figure()
    plt.axis('off')
    ax = fig.add_subplot(111)

    sep_to_plot = sep_value_arg / 2
    for rec_val in recs_arg:
        plot_rectangle(rec_val, sep_to_plot, max_area_val, ax)

    plt.axis('scaled')
    fig.tight_layout()


def plot_rectangle(rec_arg, sep_to_plot_arg, max_area_arg, ax):
    p1 = np.array([rec_arg.x1 - sep_to_plot_arg, rec_arg.y1 - sep_to_plot_arg])
    p2 = np.array([rec_arg.x1 - sep_to_plot_arg, rec_arg.y2 + sep_to_plot_arg])
    p3 = np.array([rec_arg.x2 + sep_to_plot_arg, rec_arg.y1 - sep_to_plot_arg])
    p4 = np.array([rec_arg.x2 + sep_to_plot_arg, rec_arg.y2 + sep_to_plot_arg])

    ps = np.array([p1, p2, p4, p3, p1])

    max_n = 300
    max_log = np.log2(max_n + 1)
    area_ratio = (max_n*(rec_arg.get_area()/max_area_arg))+1
    line_w = np.log2(area_ratio)/max_log
    plt.plot(ps[:, 0], ps[:, 1], linewidth=0.2*line_w + 0.08, c='r')

    rect = matplotlib.patches.Rectangle((p1[0], p1[1]), p3[0] - p1[0], p2[1] - p1[1], color='yellow', lw=0)
    ax.add_patch(rect)


if len(sys.argv) < 3:
    print('ERROR args. Needed \n[1]in_path(.json) \n[2]out_path(.jpg)')
    sys.exit()

in_path = str(sys.argv[1])      # .json
out_path = str(sys.argv[2])     # .jpg

colors_list = list(colors._colors_full_map.values())
colors_len = len(colors_list)

json_data_raw = load_from_json(in_path)

json_data = np.array(json_data_raw['data'])
sep_value = float(json_data_raw['sep_value'])


recs = []
for jd in json_data:
    recs.append(Rectangle(jd[0], jd[1], jd[2], jd[3]))


plot_rectangles(recs, sep_value)
plt.savefig(out_path, dpi=2500)

