
import sys
from lib.tools import load_from_json, Rectangle
import numpy as np


in_path = str(sys.argv[1])

json_data_raw = load_from_json(in_path)

json_data = np.array(json_data_raw['data'])
sep_value = float(json_data_raw['sep_value'])


recs = []
for jd in json_data:
    recs.append(Rectangle())


best_set = recs
array_to_save = np.zeros(shape=[len(best_set), 4])