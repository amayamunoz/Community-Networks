# Community-Networks: A GENI network topology representing community networks

Availability of computers and Internet has essentially become a universal right, yet still Internet remains inaccessible in some rural and low-income parts of the world. Commercial Internet Service Providers are essentially the only form of high-speed internet access people have, limiting the consumers' choices and setting inescapable high prices. These providers can even prevent people from getting Internet by refusing to extend network lines to certain areas, such as rural territories, as there is not much demand and they will not make significant profit. 

![Internet Use by Income](https://github.com/amayamunoz/Community-Networks/blob/master/internet_use.png)

This image shows the computer and Internet usage of households in the United States, split into 4 different income brackets. There is a huge disparity between computer/Internet usage for households with higher incomes and households with lower incomes. Households with higher incomes (>75k) have nearly 100% Internet usage or access, while households with lower incomes (<25k) have around 50%, showing that those with lower incomes often cannot obtain Internet access.

Data Source: 

Community networks have been presented as a potential solution to the problem of Internet availability. Community networks are an alternate way for underserved areas to obtain Internet connection. They are run by the users, for the users, without the need for every user to have Internet access from an ISP. Each individual person's wireless router can become a node, in which they can obtain Internet access as well as share it with others. 

![Map of Community Networks around the World] (https://github.com/amayamunoz/Community-Networks/blob/master/cnmap2.png)

This map of the world depicts some of the more well-known community networks, to show their world-wide spread. There are many other smaller networks not shown.

A popular example of one is Guifi in Spain. They are a successful community network (and the biggest) with over 20,000 nodes, stemming from a rural area of Catalonia which had no ISPs to provide to them. They have been so successful that they have even signed agreements with local government to bring Internet access to new areas. Another inspiring community network is one in Sarantaporo, Greece. This agricultural region had never had Internet access, and were basically isolated from the world, and each other. They were able to build a wireless community network that connected the many different villages in the region, to enliven their economy and allow better access to basic services like medical aid. The villages were able to communicate with each other, as well as the rest of the world through the network. The people of Sarantaporo are excited to get up in the morning and check the common website, where they can interact and organize events, and children find the villages more attractive now, whereas before they would often grow up to leave the region. There have been many similar intiatives all around the world to connect people and provide them with what many may think of as a human right, Internet access.

In my project, I create a tool to help researchers experiment on community networks. This is important because since community networks are user-run and are built from the bottom up, they have different characteristics from the conventional networks provided by ISPs. 

![A Conventional Network](https://github.com/amayamunoz/Community-Networks/blob/master/connetwork.png)

This drawing shows the heirarchy within the ISP or conventional model. Connection goes through many levels before it is passed to the public. 

![Community Networks](https://github.com/amayamunoz/Community-Networks/blob/master/commnetwork.png)

This drawing shows how, in community networks, there is little hierarchy and all of the nodes are interconnected with each other.

There are multiple benefits to using community networks over conventional ones. For one, they are generally relatively inexpensive to operate and free to use. Community networks increase consumer choice: in urban areas, there is a bit more freedom to make an individual choice in how you would like to obtain Internet, so you are not forced to use ISPs, and in rural areas, it may even be the only choice.  There is also an opportunity for increased security, privacy, and neutrality with community networks. Since everything is decentralized, it is more difficult for oppressive governments to exploit points in the network infrastructure to collect mass data or to censor some sources of information. With ISPs, there is a more centralized network, and they can control the mass majority of user's interaction. Similarly, conventional networks may accept payment from content providers to favor their traffic (a net neutrality violation) but community networks treat all traffic equally.

The decentralized model of community networks proves beneficial in crises and failures. When a node fails and goes down in a mesh/community network, it does not affect the rest of the network, as they can still obtain connection from another node. In a conventional/centralized model, if the central node goes down then all nodes lose access. For example, when Hurricane Sandy hit the East Coast and most of New York could not communicate with one another, Red Hook WiFi, a community mesh network in Brooklyn, was still up and running and able to provide a means of communication between people.


Some characteristics of community networks have a negative impact on user experience. Community networks are composed mainly of wireless links, equating to increased packet loss. Community networks are also mesh networks, leading to more latency because data has to go through multiple hops to reach a destination.

However, creators of applications and other Internet related products don't really cater their products to consumers running them on community networks, which ultimately means decreased quality for those using the network (even though they already have slower speeds). Furthermore, it would be useful to create products specifically for community network users. For instance, they would benefit from peer-to-peer video streaming where each node can stream a video content to another node, rather than each node trying to get a video individually from the internet.

To make applications for community network users, it may seem like the most accurate thing to do would be to test them directly on the CNs, but this is not a controlled environment and is not ideal for testing applications or alternative networking protocols to be deployed on them. Instead, the goal of our research is to make it easy for researchers to study the performance of community networks in a controlled environment, and use this environment to make Internet use better for them.

GENI is a research testbed where researchers can create an arbitrary configuration of computers connected by links, and then actually log into them to test and download applications. There are hundreds of nodes or virtual machines across the country at many universities that GENI researchers can gain access to from their computer.

To help researchers represent community networks on GENI, we wrote a Python script that generates a "resource specification" (RSpec) file that researchers can use to set up a network on GENI for testing. It gets data from an active community network, specifically Funk Feuer Graz in Austria, a fairly large community network with hundreds of nodes. As the data source, we downloaded a file that represents the nodes and the links of the FFGraz community network topology as a graph. 

Since the total topology includes hundreds of nodes, and it is more useful (and practical) to study small parts of it at a time, we then partition the graph into various subgraphs, separated by color in the image below. The partitioning process exploits the modularity that is characteristic of these networks: networks with high modularity have modules with dense connections between the nodes and sparse connections between nodes in different modules. So each subgraph includes nodes that are closely connected to one another, but not closely connected to nodes in other subgraphs, making them ideal to study in isolation.

![Colored CN Graph](https://raw.githubusercontent.com/amayamunoz/Community-Networks/master/Color-Graph.png)

This graph shows the topology split into communities with different colors for each community.

Next, we had to address cliques. Every node in a clique is connected to all other nodes in a clique (fully connected). In a wireless network, nodes that are all close to one another are fully connected through a single shared link. However, in the graph of the topology, it depicted these as point-to-point links, where each node had one individual link with every other node. When we represent the network on GENI, we want to represent the clique as a single shared link so that (1) traffic between one pair of nodes will affect other nodes on the link, which is more realistic, and (2) it is easier to successfully reserve the topology on GENI, since it requires fewer links overall. To solve this, our script finds all of the cliques in our subgraph and connects all of the nodes within the clique to one link.

![Subgraph selected for this example](https://github.com/amayamunoz/Community-Networks/blob/master/subgraph3.png)

Subgraph 3 from the topology. Cliques are within rectangles

Doing this, we were able to generate an accurate GENI topology of the subgraph.

![GENI Community Network Topology](https://github.com/amayamunoz/Community-Networks/blob/master/geniportal.png)

This image shows how the topology of subgraph 3 looks on GENI

# Run my experiment

There are many different python libraries you will need to reproduce this experiment. For example, community, matplotlib, seaborn, pydotplus, and networkx. To make this easier, you can reserve a single VM on GENI and log onto it and use these commands.

    sudo apt-get install python-pip
    sudo pip install networkx
    sudo apt-get install pkg-config
    sudo apt-get install libpng-dev
    sudo apt-get install libfreetype6-dev
    sudo apt-get install libjpeg8-dev 
    sudo apt-get install python-dev
    sudo pip install matplotlib
    sudo apt-get install gfortran libopenblas-dev liblapack-dev
    sudo apt-get install python-numpy python-scipy
    sudo pip install seaborn
    sudo apt-get install mercurial
    hg clone https://bitbucket.org/taynaud/python-louvain
    cd python-louvain
    sudo python setup.py install
    sudo pip install pydotplus

Then you will want to download the topology file to the node. To do this you can use this code:

    wget http://stats.ffgraz.net/topo/topology.dot.plain

If you want to use another topology file, you can just input an alternate file link there. 

Next, you will want to clone this repository, then go into the repository. To do this, you can use 

    git clone https://github.com/amayamunoz/Community-Networks.git myclone
    cd myclone
    
Once you're there, you should have the file "topology.py". You can run this python code, which will in turn produce an Rspec in an xml file called "subgraph-3.xml". If you want to change which subgraph you are using, change the integer value for the variable "subgraph". This will also change the Rspec file name and the 3 will be replaced with whichever number you chose. 

You can then upload the Rspec to GENI and reserve the resources, and you have your own community network topology!

As future work, we would like to use other sources of data on community networks to make our GENI links emulate realistic network conditions, such as packet loss, link capacity, and latency, using <code>netem</code>. 
