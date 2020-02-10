
import matplotlib.pyplot as plt
import networkx as nx

summary_groups_data_path = '/Users/Juan/django_projects/adaptive-boxes/graphs/partitions_data/boston/summary_groups.csv'



G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(1, 2)

G.number_of_nodes()
G.number_of_edges()


nx.draw(G, with_labels=True)
plt.show()

