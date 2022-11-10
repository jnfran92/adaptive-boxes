import networkx as nx
import metis
G = metis.example_networkx()
(edgecuts, parts) = metis.part_graph(G, 3)
colors = ['red','blue','green']
for i, p in enumerate(parts):
    G.node[i]['color'] = colors[p]

