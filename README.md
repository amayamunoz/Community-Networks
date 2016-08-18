# Community-Networks: A GENI network topology representing community networks

Availability of computers and Internet has increased greatly since the world wide webs onset, yet still Internet remains inaccessible in some rural and low-income parts of the world. Commercial Internet Service Provider's are essentially the only form of high-speed internet access people have, limiting the consumers choices and setting inescapable high prices. These providers can even prevent people from getting Internet by refusing to extend network lines to certain areas, usually in rural territories, as there is not much demand and they will not make significant profit. Community networks have been presented as a potential solution to the problem of Internet availability.

![Internet Use by Income](/internet-use-by-income.pdf)

This image shows the computer and Internet usage of households in the United States, split into 4 different income brackets. There is a huge disparity between computer/Internet usage for households with higher incomes and households with lower incomes. We can connect computer/Internet usage with computer/Internet access, because presumably if you have access you will have usage. Households with higher incomes (>75k) have nearly 100% Internet usage or access, while households with lower incomes (<25k) have around 50%, showing that those with lower incomes often cannot obtain Internet access.

Data Source:

Community networks are an alternate way for underserved areas to obtain Internet connection, a potential solution to the problem of availability. They are run by the users, for the users, without the need for ISPs (although they can be used to accompany ISPs). Each individual person can become a node, in which they can obtain Internet access as well as provide others with it. A popular example of one is Guifi in Spain. They are a successful community network (and the biggest) with over 20,000 nodes, stemming from a rural area of Catalonia which had no ISPs to provide to them. An inspiring community network is one in Sarantaporo, Greece. This agricultural region had never had Internet access, and were basically isolated from the world, and each other. They were able to build a wireless community network that connected the many different villages in the region, to enliven their economy and allow better access to basic services like medical aid. The villages were able to communicate with each other, as well as the rest of the world through the network. The people of Sarantaporo are excited to get up in the morning and check the common website, where they can interact and organize events, and children find the villages more attractive now, whereas before they would often grow up to leave the region. There have been many intiatives for them all around the world as an attempt to connect people and provide them with what many may think of as a human right, Internet access.

![Map of Community Networks around the World] (/cnmap.svg)

This map of the world depicts some of the more well-known community networks, to show their world-wide spread. There are many other smaller networks not shown.

Data Source:

In my research, I am attempting to emulate a community network by creating a topology for GENI based off of data from active CNs around the world. The foundation for my research stems from the fact that community networks have different characteristics from the conventional networks provided by ISPs. Since community networks are user-run and are built from the bottom up, they do not provide the same quality (speed, stability) conventional networks do. They are wireless, equating to increased packet loss. They are also mesh networks, leading to more latency because data has to go through multiple hops to reach a destination. As well, creators of applications and other Internet related products don't really cater their products to consumers running them on community networks, which ultimately means decreased quality for those using the network (even though they already have slower speeds). It would be useful to create products specifically for community network users. For instance, they would benefit from peer-to-peer video streaming where each node can stream a video content to another node, rather than each node trying to get a video individually from the internet.

![A Conventional Network](/new_view.svg)

This drawing shows the heirarchy within the ISP or conventional model. Connection goes through many levels before it is passed to the public. The public is not sure of what goes on behind the scenes, all they know is that they are getting access.

Data Source:

Though they may have various problems, there are also multiple benefits to using community networks over conventional ones. For one, they are generally cheap, although the equipment used is high level. Also pertaining to them being "high level", they are also relatively easy to set-up and use, and people with minimal tech knowledge can still become nodes. When applied to urban areas, there is a bit more freedom to make an individual choice in how you would like to obtain Internet, so you are not forced to use ISPs. When applied to rural areas, even if it is the only choice, at least there is a choice. There is also an insight for increased security and privacy with community networks. Since everything is decentralized, it is more difficult for intruders to exploit points in the network infrastructure to collect mass data. With ISPs, there is a more centralized network, and they can control the mass majority of user's interaction. Being that there are so few ISPs, it is negative to have this sort of network structure and a decentralized model is almost always better. The decentralized model of community networks proves beneficial in crises and failures. For example, when Hurricane Sandy hit the east coast and most of New York could not communicate with each other, Red Hook WiFi, a community mesh network in Brooklyn, was still up and running and able to provide a means of communication between people. As well, when a node fails and goes down in a mesh/community network, it does not affect the rest of the network, as they can still obtain connection from another node. In a conventional/centralized model, if the central node goes down then all nodes lose access. There is also the point of increased net neutrality in these networks. In the community network model, bandwidth is distributed equally and redistributed every time a new node joins. There is also no head or central node, or anyone really in control, emphasizing the "community" in community networks.

![Community Networks](/cluster_sm.svg)

This drawing shows the closeness of community networks, and how all of the nodes are interconnected with each other.

Data Source:



With this type of networks prospective advantages, and as an attempt to ameliorate the neglect for these users, we are proposing to create a network topology for GENI that represents a community network, based off of data from active CNs, specifically Funk Feuer Graz in Austria, a fairly large community network with hundreds of nodes. In doing this, progressive researchers can use our design to better understand community networks, and test their products on it so they can create applications that work more efficiently on these networks, or specifically for them. This way, people without access to ISPs or ability to pay their high prices, or even those who just want more of a choice, will receive better quality, and can be somewhat alleviated from their subpar speeds. To make applications the best for these users, it may seem like the most accurate thing to do would be to test them directly on the CNs, but this is not a controlled environment and is not ideal for testing applications to be deployed on them. Our proposed best thing to do is to create a topology that is accurately representative of CNs, giving us presumably the same results as if we had actually tested on a community network, but in a controlled environment, allowing researchers to test applications for them in any way they want, however many times they want, before actually deploying them. Hopefully, this can help to make these networks more efficient for the users, and further the growth of them.

To do this, I first downloaded a dot file for a graph of a community network topology from FFGraz. We were able to read in the dot file using pythons networkx module. Using the file, we wrote a code that generated a graph of the topology. We then partitioned the graph into various subgraphs, separated by color. We did this because we don't really need the whole topology with hundreds of nodes, we could just use a sample from it. As well, the GENI testbed would most likely be unable to reserve enough resources for the whole topology, making researchers unable to test applications and actually do what we set out to do.

![Colored CN Graph](/Color-Graph.svg)

This graph shows the topology split into communities with different colors for each community.

Data Source:

Within the code, we were then able to select a community (subgraph) and isolate it from the rest of the topology.

![Subgraph selected for this example](/subgraph-3.svg)

Subgraph 3 from the topology

Data Source: 





