# Community-Networks: A GENI network topology representing community networks

Availability of computers and Internet has essentially become a universal right, yet still Internet remains inaccessible in some rural and low-income parts of the world. Commercial Internet Service Providers are essentially the only form of high-speed internet access people have, limiting the consumers' choices and setting inescapable high prices. These providers can even prevent people from getting Internet by refusing to extend network lines to certain areas, such as rural territories, as there is not much demand and they will not make significant profit. 

![Internet Use by Income](/internet-use-by-income.pdf)

This image shows the computer and Internet usage of households in the United States, split into 4 different income brackets. There is a huge disparity between computer/Internet usage for households with higher incomes and households with lower incomes. Households with higher incomes (>75k) have nearly 100% Internet usage or access, while households with lower incomes (<25k) have around 50%, showing that those with lower incomes often cannot obtain Internet access.

Data Source:

Community networks have been presented as a potential solution to the problem of Internet availability. Community networks are an alternate way for underserved areas to obtain Internet connection. They are run by the users, for the users, without the need for every user to have Internet access from an ISP. Each individual person's wireless router can become a node, in which they can obtain Internet access as well as share it with others. 

![Map of Community Networks around the World] (/cnmap.svg)

This map of the world depicts some of the more well-known community networks, to show their world-wide spread. There are many other smaller networks not shown.

A popular example of one is Guifi in Spain. They are a successful community network (and the biggest) with over 20,000 nodes, stemming from a rural area of Catalonia which had no ISPs to provide to them. They have been so successful that they have even signed agreements with local government to bring Internet access to new areas. Another inspiring community network is one in Sarantaporo, Greece. This agricultural region had never had Internet access, and were basically isolated from the world, and each other. They were able to build a wireless community network that connected the many different villages in the region, to enliven their economy and allow better access to basic services like medical aid. The villages were able to communicate with each other, as well as the rest of the world through the network. The people of Sarantaporo are excited to get up in the morning and check the common website, where they can interact and organize events, and children find the villages more attractive now, whereas before they would often grow up to leave the region. There have been many similar intiatives all around the world to connect people and provide them with what many may think of as a human right, Internet access.

In my project, I create a tool to help researchers experiment on community networks. This is important because since community networks are user-run and are built from the bottom up, they have different characteristics from the conventional networks provided by ISPs. 

![A Conventional Network](/new_view.svg)

This drawing shows the heirarchy within the ISP or conventional model. Connection goes through many levels before it is passed to the public. 

Data Source:

![Community Networks](/cluster_sm.svg)

This drawing shows how, in community networks, there is little hierarchy and all of the nodes are interconnected with each other.

Data Source:


There are multiple benefits to using community networks over conventional ones. For one, they are generally relatively inexpensive to operate and free to use. Community networks increase consumer choice: in urban areas, there is a bit more freedom to make an individual choice in how you would like to obtain Internet, so you are not forced to use ISPs, and in rural areas, it may even be the only choice.  There is also an opportunity for increased security, privacy, and neutrality with community networks. Since everything is decentralized, it is more difficult for oppressive governments to exploit points in the network infrastructure to collect mass data or to censor some sources of information. With ISPs, there is a more centralized network, and they can control the mass majority of user's interaction. Similarly, conventional networks may accept payment from content providers to favor their traffic (a net neutrality violation) but community networks treat all traffic equally.

The decentralized model of community networks proves beneficial in crises and failures. When a node fails and goes down in a mesh/community network, it does not affect the rest of the network, as they can still obtain connection from another node. In a conventional/centralized model, if the central node goes down then all nodes lose access. For example, when Hurricane Sandy hit the East Coast and most of New York could not communicate with one another, Red Hook WiFi, a community mesh network in Brooklyn, was still up and running and able to provide a means of communication between people.


Some characteristics of community networks have a negative impact on user experience. Community networks are composed mainly of wireless links, equating to increased packet loss. Community networks are also mesh networks, leading to more latency because data has to go through multiple hops to reach a destination.

However, creators of applications and other Internet related products don't really cater their products to consumers running them on community networks, which ultimately means decreased quality for those using the network (even though they already have slower speeds). Furthermore, it would be useful to create products specifically for community network users. For instance, they would benefit from peer-to-peer video streaming where each node can stream a video content to another node, rather than each node trying to get a video individually from the internet.


With this type of networks prospective advantages, and as an attempt to ameliorate the neglect for these users, we are proposing to create a network topology for GENI that represents a community network, based off of data from active CNs, specifically Funk Feuer Graz in Austria, a fairly large community network with hundreds of nodes. In doing this, progressive researchers can use our design to better understand community networks, and test their products on it so they can create applications that work more efficiently on these networks, or specifically for them. This way, people without access to ISPs or ability to pay their high prices, or even those who just want more of a choice, will receive better quality, and can be somewhat alleviated from their subpar speeds. To make applications the best for these users, it may seem like the most accurate thing to do would be to test them directly on the CNs, but this is not a controlled environment and is not ideal for testing applications to be deployed on them. Our proposed best thing to do is to create a topology that is accurately representative of CNs, giving us presumably the same results as if we had actually tested on a community network, but in a controlled environment, allowing researchers to test applications for them in any way they want, however many times they want, before actually deploying them. Hopefully, this can help to make these networks more efficient for the users, and further the growth of them.

To do this, I first downloaded a dot file for a graph of a community network topology from FFGraz. We were able to read in the dot file using pythons networkx module. Using the file, we wrote a code that generated a graph of the topology. We then partitioned the graph into various subgraphs, separated by color. We did this because we don't really need the whole topology with hundreds of nodes, we could just use a sample from it. As well, the GENI testbed would most likely be unable to reserve enough resources for the whole topology, making researchers unable to test applications and actually do what we set out to do.

![Colored CN Graph](/Color-Graph.svg)

This graph shows the topology split into communities with different colors for each community.

Data Source:

Within the code, we were then able to select a community (subgraph) and isolate it from the rest of the topology.

![Subgraph selected for this example](/subgraph-3.svg)

Subgraph 3 from the topology

Data Source: 

Next, the problem we had to address were cliques, areas of fully interconnected nodes. Every node in a clique is connected to all other nodes in a clique. The issue was that in the graph of the topology, it depicted these cliques as point-to-point links, where each node had one individual link with every other node. However, in a wireless network this is not the case. What was represented by point-to-point links are in reality many interfaces on one link. This is because it is wireless, and each node is within the same network, therefore it is already given that they are connected to each other. This also helps us to get our topology reserved on GENI, since it won't be as congested. To solve this we wrote our code to use networkx to find all of the cliques in our subgraph and connect all of the nodes within the clique to one link, rather than creating several links.

Another problem we encountered was what to do when adding new nodes or when nodes fail, since it is a mesh network where everyone is connected to one another. To account for this, we added a routing protocol called Babel to all of our nodes. If one node or interface is down, Babel will reroute paths so that each node can still reach all others. If a new node is added or a new interface is put up, Babel will find the best way to incorporate that node into the network so it can reach all other nodes.  

Doing this, we were able to generate an accurate and stable GENI topology of the subgraph.

![GENI Community Network Topology](/geni-portal-full.svg)

This image shows how the topology of subgraph 3 looks on GENI

Data Source: 

