import networkx as nx
import metis
# G = metis.example_networkx()

G = nx.Graph()
nx.add_star(G, [0, 1, 2, 3, 4])
nx.add_path(G, [4, 5, 6, 7, 8])
nx.add_star(G, [8, 9, 10, 11, 12])
nx.add_path(G, [6, 13, 14, 15])
nx.add_star(G, [15, 16, 17, 18])

(edgecuts, parts) = metis.part_graph(G, 3)




colors = ['red','blue','green']
for i, p in enumerate(parts):
    G.node[i]['color'] = colors[p]

