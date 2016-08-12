import geni.rspec.pg as PG
import geni.rspec.egext as EGX
import geni.rspec.igext as IGX
import community
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

r = PG.Request()
G = nx.Graph(nx.drawing.nx_pydot.read_dot("topology.dot.plain")) #newfile.dot
partition = community.best_partition(G)
max(partition.values()) + 1
nodebunch = [node for node in G.nodes() if partition[node]==3]
H = G.subgraph(nodebunch)

vms = {}
for node in H.nodes():
	if H.degree(node) > 10:
		#will name supernode-x if it has over 10 links attached to it
		igvm = IGX.XenVM("supernode-%s" % node)
	else:
		igvm = IGX.XenVM("node-%s" % node)
	vms[node] = igvm
	
cl = list(nx.find_cliques(H))
links = []
edgeno = 0
for clique in cl:
    links.insert(edgeno, PG.LAN('lan%d' % edgeno))
    links[edgeno].bandwidth = 10000
    edgeno += 1
