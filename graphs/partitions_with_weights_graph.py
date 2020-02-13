
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
from networkx.readwrite import json_graph, write_gexf
from matplotlib import pylab


summary_groups_data_path = '/Users/Juan/django_projects/adaptive-boxes/graphs/partitions_data/hall/summary_groups.csv'
x_units_path = '/Users/Juan/django_projects/adaptive-boxes/graphs/partitions_data/hall/x_units.csv'
y_units_path = '/Users/Juan/django_projects/adaptive-boxes/graphs/partitions_data/hall/y_units.csv'


summary_groups = pd.read_csv(summary_groups_data_path)
x_units = pd.read_csv(x_units_path)
y_units = pd.read_csv(y_units_path)


# Getting Codes x_units
codes = []
for iuy in x_units.iterrows():
    g_tmp = iuy[1]['group_0']
    p_tmp = iuy[1]['partition_0']
    code_1 = str(g_tmp) + "_" + str(p_tmp)
    # print(code_1)

    g_tmp = iuy[1]['group_1']
    p_tmp = iuy[1]['partition_1']
    code_2 = str(g_tmp) + "_" + str(p_tmp)
    # print(code_2)
    codes.append((code_1, code_2))


codes_df = pd.DataFrame(codes)

x_units['p0_code'] = codes_df[0]
x_units['p1_code'] = codes_df[1]


# Getting Codes y_units
codes = []
for iuy in y_units.iterrows():
    g_tmp = iuy[1]['group_0']
    p_tmp = iuy[1]['partition_0']
    code_1 = str(g_tmp) + "_" + str(p_tmp)
    # print(code_1)

    g_tmp = iuy[1]['group_1']
    p_tmp = iuy[1]['partition_1']
    code_2 = str(g_tmp) + "_" + str(p_tmp)
    # print(code_2)
    codes.append((code_1, code_2))


codes_df = pd.DataFrame(codes)

y_units['p0_code'] = codes_df[0]
y_units['p1_code'] = codes_df[1]



gs_tmp = x_units.groupby('p0_code')
p0_keys_tmp = list(gs_tmp.groups.keys())

g_tmp = gs_tmp.get_group('88_0')




gs_tmp = x_units.groupby('p1_code')
p1_keys_tmp = list(gs_tmp.groups.keys())



global_keys = []
global_keys.extend(p0_keys_tmp)
global_keys.extend(p1_keys_tmp)


def remove_duplicates(l):
    return list(set(l))


global_keys_no_duplicates = remove_duplicates(global_keys)




n_total_nodes = summary_groups.shape[0]




# Creating Graphs
G = nx.Graph()
# n_total_nodes = summary_groups['n_partitions'].sum()
n_total_nodes = summary_groups.shape[0]

H = nx.path_graph(n_total_nodes)
G.add_nodes_from(H)


for idx, row in x_units.iterrows():
    # print(row)
    gi_0 = row['group_0']
    gj_0 = row['partition_0']
    gi_1 = row['group_1']
    gj_1 = row['partition_1']
    G.add_edge(gi_0, gi_1)


for idx, row in y_units.iterrows():
    # print(row)
    gi_0 = row['group_0']
    gj_0 = row['partition_0']
    gi_1 = row['group_1']
    gj_1 = row['partition_1']
    G.add_edge(gi_0, gi_1)


print(G.number_of_nodes())
print(G.number_of_edges())


options = {
     'node_color': 'yellow',
     'node_size': 80,
     'edge_color': 'red',
     'width': 0.5,
     'font_size': 8,
     'font_color': 'black',
}

# save_graph(G, "./my_graph.pdf")

# nx.draw(G, **options)
nx.draw(G, with_labels=True, **options)
plt.show()

nx.write_gexf(G, "/Users/Juan/django_projects/adaptive-boxes/graphs/gexf/hall.gexf")

# Info
print(nx.info(G))
