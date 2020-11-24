import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# K5
for i in range (5):
    for j in range (5):
        # No weight per edge
        G.add_edge(i, j)

mtx = nx.adjacency_matrix(G)

nx.draw(G)
plt.show()