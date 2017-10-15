# The Effect of Clustering on the Emergence of Cooperation in the Spatial Prisoner's Dilemma

Noah Rivkin, Changjun Lim

## Abstract:

We attempt to reproduce and expand upon the findings of Masuda and Aihara [1]. Masuda and Aihara's work examines the spatial prisoner's dilemma on small world graphs. They found that cooperative behavior emerged in a wide range of conditions. We replicate their experiment and find qualitatively similar results, but under a smaller range of conditions. We also expand on their original work by incorporating additional types of small world graphs. They had used only Watts-Strogatz type graphs, while we test Holmes-Kim graphs. Masuda and Aihara suggest that their work explains why small-world networks are so prevalent in society. They also suggest that one reason why cooperation does not always dominate could be that the rewards for defection are too high. Our analysis suggests that their results do not hold under preferential attachment, and provides an alternative explanation of real world examples where cooperation is not dominant.


## 

We find cooperation within groups in every ecological and social system. But in game theory, the prisoner's dilemma describes a situation in which each defection is the dominant strategy for each individual, but mutual defection leads to mutually undesirable situation. In prisoner's dilemma, there are two strategies, cooperation(C) or defection(D). The players choose one of the strategies every step. A player choosing C receives R(reward) or S(sucker) and a player choosing D receives T(temptation) or P(Punishment) according to the opponent chooses C or D respectively. Since T > R > P > S is given, defection is the best selection for each player regardless of the opponent's choice. Attempts have been made to resolve the dilemma, including iterated games [2] and spatial games [1, 3].

Masuda and Aihara make a model where every node of a network is a player and in each step, a player plays a single prisoner's dilemma game against each of its neighbors. Then after every player sums their points, they change their strategy to that of their the most successful neighbor(if it is best, its strategy holds) for the next step. Masuda and Aihara assume T > 1, R = 1, P = S = 0. They consider rewired regular graphs and rewired square lattice graphs using Moore neighborhoods. They set n, the number of nodes, to 3600. They ensure each node has the 8 neighbors in all graphs by keeping the degree of each node constant when they rewire graphs. 





In order to validate our model, we attempt to show that it shares behavior with Masuda and Aihara's[1] model. To do this, we test what values of T lead to cooperation. In their work, they used a rewired regular graph with n=3600 and k=8, and determined the percentage of the population that was cooperative for different values of T. They found a critical point at T=2.25 for p=0 and p=0.01. When we attempt to reproduce their results we find qualitative similarities, but a critical point of T=2 for p=0 and p=0.01. The transition region is 1.999<T<2, which is smaller than we expect. We also conduct the experiment using a 60 by 60 lattice. Masuda and Aihara found 4 distinct regimes, the last of which showed defection to be completely dominant after T=2.25. As before, our findings are qualitatively similar, but with only 3 regimes and lower values of T. 

| ![figure1_a](images/fig1_a.png "Fig. 1.(a)") | ![figure1_b](images/fig1_b.png "Fig. 1.(b)") | ![figure1_c](images/SpatialPD_Fig1.gif "Fig. 1.(c)") |
|:----------:|:----------:|:----------:|
| **Fig. 1.(a)** | **Fig. 1.(b)**|

| ![figure1_c](images/SpatialPD_Fig1.gif "Fig. 1.(c)") |
|:----------:|
|**Fig. 1.(c):** original results|


We are unable to determine the reason our results differ from the original experiments. Rewiring is not present when p=0, but our findings still vary. One possibility is that the initial distribution of cooperators is responsible. However, averaging the results over 10 trials makes this unlikely.




 
In the first experiment, we observed that there are 3 regimes after stabilization. In the second regime, the proportion of cooperators decreases as rewiring parameter p increases, that is, clustering coefficient decreases. We graph the proportion of cooperator over time to check the tendency of the network over time. We simulate it by giving 3 values of T and c<sub>0</sub>(the initial cooperator ratio) pair for each regime and changing p value with 0, 0.001, 0.01, 0.1, and 0.8. We set the first condition for Fig 2.(a) and (d) as T = 1.1 and c<sub>0</sub> = 0.1 because cooperators are dominant in the first regime. The second condition for Fig 2.(b) and (e) is T = 1.7 and c<sub>0</sub> = 0.5. The third condition for Fig 2.(c) and (f) is T = 3 and c<sub>0</sub> = 0.995 since defectors are dominant.
 
Unlike Masuda and Aihara, who observed that cooperators dominate in the first condition, our results show that the proportion of cooperators converges to small values in many of the graphs. The proportion of cooperators after transient behavior increases when p is large in Fig. 2(a), and small p in Fig. 2(d). If a cooperator is among defectors, it will always be dominated by the defectors. So cooperators must be clustered at the beginning in order to dominate the network. However, when the initial population of cooperators is low, the cooperators are surrounded by defectors, so defectors dominate.

The graphs have about half value after transient for Fig2. (b) and (e). 
In the third condition for Fig. 2(c) and (f), the cooperators ratio converge to 0 and the graph converges faster with bigger p as we expected. Since the path length decreases as p increases, the defector spreads faster with bigger p.

| ![figure2_a](images/fig2_a.png "Fig. 2.(a)") | ![figure2_b](images/fig2_b.png "Fig. 2.(b)") | ![figure2_c](images/fig2_c.png "Fig. 2.(c)") |
|:----------:|:----------:|:----------:|
| **Fig. 2.(a)** | **Fig. 2.(b)** | **Fig. 2.(c)** |

| ![figure2_d](images/fig2_d.png "Fig. 2.(d)") | ![figure2_e](images/fig2_e.png "Fig. 2.(e)") | ![figure2_f](images/fig2_f.png "Fig. 2.(f)") |
|:----------:|:----------:|:----------:|
| **Fig. 2.(d)** | **Fig. 2.(e)** | **Fig. 2.(f)** |

| ![figure2_g](images/SpatialPD_Fig2.gif "Fig. 2.(g)") |
|:----------:|
| **Fig. 2.(g):** original results|


(Expansion - not yet)

-- description

-- figure with caption

-- reasoning/interpretation

Conclusions:


## Annotated Bibliography:

[1] [**Spatial prisoner’s dilemma optimally played in small-world networks**](http://www.sciencedirect.com/science/article/pii/S0375960103006935#bBIB002)

Masuda, N., & Aihara, K. (2003). Spatial prisoner's dilemma optimally played in small-world networks. Physics Letters A, 313(1), 55-61.

Masuda and Aihara simulate an iterated prisoners dilemma with automata that interact only if they are connected on a graph. They simulate this on different types of networks, including regular graphs, lattices, and small-world networks. They find that small world networks produce cooperation to the greatest extent. They also investigate the effects of noise on the system, and consider the robustness of cooperation on the different networks.

[2] [**The Further Evolution of Cooperation**](http://www.jstor.org/stable/1702320)

Axelrod, R., & Dion, D. (1988). The further evolution of cooperation. Science, 242(4884), 1385-1390.

Axelrod and Douglas argue that evolution can produce cooperation as a trait, even in situations where defection is a dominant strategy in a non-iterated version of the situation. They expand on the prisoner's dilemma tournament model used in Axelrods original tournament to incorporate evolutionary aspects. In the new model automata are constructed from a set of instructions, and then they interact with other automata as is the case in the older model. However, in addition to altering the population of each type of automata, the automata exchange instructions (chromosomes) or randomly alter a single instruction (mutation). Axelrod and Douglas conclude that cooperation can emerge from randomized evolution.

[3] [**A simple rule for the evolution of cooperation on graphs**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2430087/)

Ohtsuki, H., Hauert, C., Lieberman, E., & Nowak, M. A. (2006). A simple rule for the evolution of cooperation on graphs. Nature, 441(7092), 502.

Ohtsuki, Hauert, Lieberman, and Nowak are motivated from that cooperation is the property of all biological system. They propose the simple graph model in which natural selection prefers cooperation in the certain condition. They assume vertice are divided into two types, cooperators who pay a cost for neighbors to receive a benefit and defectors who only receive benefits from cooperators. They simulate for various graph types(cycle, lattice, random regular graph, random graph and scale-free network) and find the condition that cooperators spread throughout the graph. They find that the fewer connections, the more cooperation in their model.
