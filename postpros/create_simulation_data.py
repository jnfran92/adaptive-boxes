
##
# Create simulation data from adaptive boxes results
##

import numpy as np

from adabox.tools import load_from_json
from postpros.lib.groups_creator import create_groups

# plt.ioff()


in_path = "/Users/Juan/django_projects/adaptive-boxes/results/complex.json"      # .json
out_path = "./out"    # .jpg


json_data_raw = load_from_json(in_path)

json_data = np.array(json_data_raw['data'])
sep_value = float(json_data_raw['sep_value'])


a ,b =create_groups(json_data, sep_value)


print(b)
