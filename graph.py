import community
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
G = nx.Graph(nx.drawing.nx_pydot.read_dot("topology.dot.plain"))
partition = community.best_partition(G)
colors = sns.color_palette("hls", max(partition.values())+1)
#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
for com in set(partition.values()) :
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 30,
                                node_color = colors[com])


nx.draw_networkx_edges(G,pos, alpha=0.5, width=0.5)
plt.savefig("Color-Graph.svg", format="SVG")

plt.clf()

nodebunch = [node for node in G.nodes() if partition[node]==3]
H = G.subgraph(nodebunch)
nx.draw_spring(H, node_size = 60, node_color = colors[3])
plt.savefig("subgraph-3.svg", format="SVG")
