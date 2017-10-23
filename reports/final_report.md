# The Effect of Clustering on the Emergence of Cooperation in the Spatial Prisoner's Dilemma

Noah Rivkin, Changjun Lim

## Abstract:

We attempt to reproduce and expand upon the findings of Masuda and Aihara [1]. Masuda and Aihara's work examines the spatial prisoner's dilemma on small world graphs. They found that cooperative behavior emerged in a wide range of conditions. We replicate their experiment and find qualitatively similar results, but under a smaller range of conditions. We also expand on their work by incorporating additional types of small world graphs. They used only Watts-Strogatz type graphs, while we test Holmes-Kim graphs [2]. Masuda and Aihara suggest that their work explains why small-world networks are so prevalent in society. They also suggest that one reason why cooperation does not always dominate could be that the rewards for defection are too high. Our analysis suggests that their results do not hold under preferential attachment, and provides an alternative explanation of real world examples where cooperation is not dominant.


## 

We find cooperation within groups in every ecological and social system. But in game theory, the prisoner's dilemma describes a situation in which defection is the dominant strategy for each individual, but mutual defection leads to mutually undesirable situation. In prisoner's dilemma, there are two strategies, cooperation(C) or defection(D). The players choose one of the strategies every step. A player choosing C receives R(reward) or S(sucker) and a player choosing D receives T(temptation) or P(Punishment) depending on whether the opponent chooses C or D respectively. Since T > R > P > S is given, defection is the best selection for each player regardless of the opponent's choice. Attempts have been made to resolve the dilemma, including iterated games [3] and spatial games [1, 4].

Masuda and Aihara make a model where every node of a network is a player and in each step, a player plays a single prisoner's dilemma game against each of its neighbors. Then after every player sums their points, they change their strategy to that of their the most successful neighbor(if it is best, its strategy holds) for the next step. Masuda and Aihara use T > 1, R = 1, P = S = 0. They consider rewired regular graphs and rewired square lattice graphs using Moore neighborhoods. They set n, the number of nodes, to 3600. They ensure each node has 8 neighbors in all graphs by keeping the degree of each node constant when they rewire graphs. 





In order to validate our implementation, we attempt to show that it shares behavior with Masuda and Aihara's [1] model. To do this, we test what values of T lead to cooperation. In their work, they used a rewired regular graph with n=3600 and k=8, and determined the percentage of the population that was cooperative for different values of T. They found a critical point at T=2.25 for p=0 and p=0.01. When we attempt to reproduce their results we find qualitative similarities, but a critical point of T=2 for p=0 and p=0.01. The transition region is 1.999<T<2, which is smaller than we expect. We also conduct the experiment using a 60 by 60 lattice. Masuda and Aihara found 4 distinct regimes, the last of which showed defection to be completely dominant after T=2.25. As before, our findings are qualitatively similar, but with only 3 regimes and lower values of T. 

| ![figure1_a](images/fig1_a.png "Fig. 1.(a)") | ![figure1_b](images/LatticeFig1b.png "Fig. 1.(b)") | 
|:----------:|:----------:|
| **Fig. 1.(a):** proportion of cooperators on a rewired regular graph with n=3600, k=8 after 100 steps| **Fig. 1.(b):** proportion of cooperators on a rewired lttice graph after 100 steps|

| ![figure1_c](images/SpatialPD_Fig1.gif "Fig. 1.(c)") |
|:----------:|
|**Fig. 1.(c):** Masuda and Aihara's results. |


We are unable to determine the reason our results differ from the original experiments. Rewiring is not present when p=0, but our findings still vary. One possibility is that the initial distribution of cooperators is responsible. In order to reduce the likelihood that the original distribution was influencing the output we ran the experiment with ten different randomly generated initial distributions, and averaged the proportion of cooperators at each timestep. 


Figure 1 shows the proportion of cooperators that emerges for different values of T, but it does not show how the networks reached thier final conditions. In order to better understand the process by which the networks change over time we graph the propertion of cooperators, %C, in a network over time. We begin with a network with a initial cooperator ratio, c<sub>0</sub>, and graph the value of %C at each time step. Since we can divide the 3 following regimes, we chose the T value in each regime(T = 1.1, 1.7, 3.0).

 \(i) For small T, cooperation dominates regardless of p.<br />
 \(ii) Roughly for 1.2 ≤ b ≤ 2.1, the number of cooperators depends on p. <br />
 \(iii) For large T, all player eventually becomes a defector.


| ![figure2_a](images/fig2_a.png "Fig. 2.(a)") | ![figure2_b](images/fig2_b.png "Fig. 2.(b)") | ![figure2_c](images/fig2_c.png "Fig. 2.(c)") |
|:----------:|:----------:|:----------:|
| **Fig. 2.(a):** Watts-Strogatz graph, T=1.1, c<sub>0</sub>=0.1 | **Fig. 2.(b):** Watts-Strogatz graph, T=1.7, c<sub>0</sub> = 0.5| **Fig. 2.(c):** Watts-Strogatz graph, T=3.0 , c<sub>0</sub>=0.995|

| ![figure2_d](images/fig2_d.png "Fig. 2.(d)") | ![figure2_e](images/fig2_e.png "Fig. 2.(e)") | ![figure2_f](images/fig2_f.png "Fig. 2.(f)") |
|:----------:|:----------:|:----------:|
| **Fig. 2.(d):** Lattice graph, T=1.1, c<sub>0</sub>=0.1| **Fig. 2.(e):** Lattice graph, T=1.7, c<sub>0</sub>=0.5| **Fig. 2.(f):** Lattice graph, T=3.0, c<sub>0</sub>=0.995|

| ![figure2_g](images/SpatialPD_Fig2.gif "Fig. 2.(g)") |
|:----------:|
| **Fig. 2.(g):** Masuda and Aihara's results from the same initial conditions|


All of the graphs converge at some value of %C. Once the value of %C stops changing we consider the behavior of the network to be stable. Before reaching a stable state the graph exhibits transient behavior.

Unlike the results of Masuda and Aihara in which cooperators always dominate in the first regime, our results show that the proportion of cooperators converges to small values in many of the graphs. Only graphs with high p converge to the high percentage of cooperators. Also, in the second regime, defection is always dominant differently from the original result.

We could think that the initial population of cooperators is the major factor as well as T value. If a cooperator is among defectors, it will always chose to be a defector. So cooperators must be clustered at the beginning in order to dominate the network. However, when the initial population of cooperators is low, many of cooperators are surrounded by defectors and defectors eventually dominate in the population.

In Fig. 2(c) and (f), the cooperator's ratio converge to 0 faster with bigger p. This result match with that of Masuda and Aihara. As the path length decreases as p increases, the defector spreads throughout the population more rapidly with a larger p.

Masuda and Aihara only considered graphs with the constant degree. We use power-law graphs formed by preferential attachment to see if hub-spoke graph architecture leads to different results. We run the same procedure we used for regular and lattice graphs on Holme-Kim graphs [2].

In HK graphs p is the likelihood that an additional triangle will be added to a node on its creation, leading to a greater clustering coefficient. Unlike the previous graphs, sweeping T does not lead to distinct regimes. Instead, we observe that while the proportion of cooperators tends to be less for higher T values, the percentage of cooperators does not converge. Higher values of p, which correspond to greater clustering, lead to increased cooperation. This is shown in Figure 3.



| ![figure3_b](images/fig3_b.png "Fig. 3.(b)") | 
|:----------:|
| **Fig. 3**|


When considering the percentage of cooperators over time, as shown in Fig. 4, we observed behavior different from that displayed in Fig. 2. The value of T does not affect the percentage of cooperators as it does in Fig. 2. The number of cooperators stabilizes within ten timesteps. The success of the cooperator is dependent on the initial population of cooperators.


| ![figure4_a](images/fig4_a.png "Fig. 4.(a)") | ![figure2_b](images/fig4_b.png "Fig. 4.(b)") | ![figure4_c](images/fig4_c.png "Fig. 4.(c)") |
|:----------:|:----------:|:----------:|
| **Fig. 4.(a)** | **Fig. 4.(b)** | **Fig. 4.(c)** |


We believe that the dependency on initial population is a property of the hub-spoke architecture. A single defector on a hub can result in many of the nodes at the end of the hubs' spokes becoming defectors. Similarly, a single cooperator at a hub can spread rapidly. Because the hub node has so many neighbors the node on the hub has a much higher possible score than a node elsewhere. As a result, the nodes on hubs quickly come to dominate the part of the graph near them. The importance of the hubs results in the sensitivity to initial populations. The percentage of the hubs initially populated by cooperators is directly proportional to the percentage of the initial population that are cooperators. The potential score from a hub is high enough to overwhelm the dependency on T seen in Fig. 2.


This dependency on initial conditions provides an alternative to Masuda and Aihara's explanation of the emergence of cooperation. Instead of cooperation in a network being dependent on the value of T, it is instead dependent on the initial proportion of cooperators. This resistance to change in networks formed by preferential attachment could be responsible for many behaviors in real world social networks.

## Annotated Bibliography:

[1] [**Spatial prisoner’s dilemma optimally played in small-world networks**](http://www.sciencedirect.com/science/article/pii/S0375960103006935#bBIB002)

Masuda, N., & Aihara, K. (2003). Spatial prisoner's dilemma optimally played in small-world networks. Physics Letters A, 313(1), 55-61.

Masuda and Aihara simulate an iterated prisoners dilemma with automata that interact only if they are connected on a graph. They simulate this on different types of networks, including regular graphs, lattices, and small-world networks. They find that small world networks produce cooperation to the greatest extent. They also investigate the effects of noise on the system, and consider the robustness of cooperation on the different networks.

[2] [**Growing scale-free networks with tunable clustering**](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.65.026107)

Holme, P., & Kim, B. J. (2002). Growing scale-free networks with tunable clustering. Physical review E, 65(2), 026107.

Holme and Kim propose the model constructing the scale-free networks with the high clustering. Their model extends the Barabasi-Albert(BA) model by adding a 'triad formation' step which yields high clustering coefficient to a BA network. They control the clustering coefficient by changing the average number of triad formation per step.

[3] [**The Further Evolution of Cooperation**](http://www.jstor.org/stable/1702320)

Axelrod, R., & Dion, D. (1988). The further evolution of cooperation. Science, 242(4884), 1385-1390.

Axelrod and Douglas argue that evolution can produce cooperation as a trait, even in situations where defection is a dominant strategy in a non-iterated version of the situation. They expand on the prisoner's dilemma tournament model used in Axelrods original tournament to incorporate evolutionary aspects. In the new model automata are constructed from a set of instructions, and then they interact with other automata as is the case in the older model. However, in addition to altering the population of each type of automata, the automata exchange instructions (chromosomes) or randomly alter a single instruction (mutation). Axelrod and Douglas conclude that cooperation can emerge from randomized evolution.

[4] [**A simple rule for the evolution of cooperation on graphs**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2430087/)

Ohtsuki, H., Hauert, C., Lieberman, E., & Nowak, M. A. (2006). A simple rule for the evolution of cooperation on graphs. Nature, 441(7092), 502.

Ohtsuki, Hauert, Lieberman, and Nowak are motivated from that cooperation is the property of all biological system. They propose the simple graph model in which natural selection prefers cooperation in the certain condition. They assume vertice are divided into two types, cooperators who pay a cost for neighbors to receive a benefit and defectors who only receive benefits from cooperators. They simulate for various graph types(cycle, lattice, random regular graph, random graph and scale-free network) and find the condition that cooperators spread throughout the graph. They find that the fewer connections, the more cooperation in their model.
