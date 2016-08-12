import geni.rspec.pg as PG
import geni.rspec.egext as EGX
import geni.rspec.igext as IGX
import community
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

r = PG.Request()
G = nx.Graph(nx.drawing.nx_pydot.read_dot("newfile.dot")) #newfile.dot
partition = community.best_partition(G)
max(partition.values()) + 1
nodebunch = [node for node in G.nodes() if partition[node]==3]
H = G.subgraph(nodebunch)

nodeno = 0
vms = {}
for node in H.nodes():
	if H.degree(node) > 10:
		#will name supernode-x if it has over 10 links attached to it
		igvm = IGX.XenVM("supernode-%d" % nodeno)
	else:
		igvm = IGX.XenVM("node-%d" % nodeno)
	vms[nodeno] = igvm
	nodeno += 1

links = []
edgeno = 0
for edge in H.edges():
    links.insert(edgeno, PG.LAN('lan%d' % edgeno))
    links[edgeno].bandwidth = 10000
    edgeno += 1
