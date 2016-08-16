import geni.rspec.pg as PG
import geni.rspec.egext as EGX
import geni.rspec.igext as IGX
import community
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

r = PG.Request()
setupcmd='wget -qO- https://git.io/v6m6o | bash /dev/stdin'

G = nx.Graph(nx.drawing.nx_pydot.read_dot("topology.dot.plain")) #newfile.dot
partition = community.best_partition(G)
max(partition.values()) + 1

subgraphno = 3
nodebunch = [node for node in G.nodes() if partition[node]==subgraphno]
H = G.subgraph(nodebunch)

vms = {}
for node in H.nodes():
	if H.degree(node) > 10:
		#will name supernode-x if it has over 10 links attached to it
		igvm = IGX.XenVM("supernode-%s" % node.replace(".", "-").replace("/", "-"))
	else:
		igvm = IGX.XenVM("node-%s" % node.replace(".", "-").replace("/", "-"))
	igvm.addService(PG.Execute(shell="/bin/bash", command=setupcmd))
	vms[node] = igvm
        r.addResource(igvm)
	
cl = list(nx.find_cliques(H))
links = []
edgeno = 0
for clique in cl:
    links.insert(edgeno, PG.LAN('lan%d' % edgeno))
    links[edgeno].bandwidth = 10000
    nodeno = 0
    for x in clique:
    	iface = vms[x].addInterface("if%s" % str(edgeno) + "-" + str(nodeno)) #duplicate interface names error
    	links[edgeno].addInterface(iface)
        nodeno += 1
    r.addResource(links[edgeno])
    edgeno += 1

r.writeXML("subgraph-%s.xml" % subgraphno)
