**The Emergence of Cooperation in the Spatial Prisoner's Dilemma and Snowdrift Dilemma**

Noah Rivkin, Changjun Lim

[abstract]

We will recreate the experiment described by Masuda and Aihara [1], in which a spatial version of the prisoner's dilemma is played on small world networks. This is similar to the experiment conducted by Ohtsuki, Hauert, Lieberman, and Nowak[2]. We then intend to extend the experiment by altering the payoffs, and the strategies, to replicate the snowdrift dilemma, as described by Santos and Pacheco[3]. Time allowing, we may also implement more complex strategies than all-D and all-C. These strategies may require the implementation of an iterated dilemma; while this is a major extension from the original work, we believe it might demonstrate that the conclusions found by Axelrod and Douglas hold in a spatial tournament in addition to a random tournament[4].

[end of abstract]

During the first week, we intend to recreate the experiment conducted in [Spatial prisoner's dilemma optimally played in small-world networks], by Masuda and Aihara [1]. In the experiment a network is created, where each node represents either cooperation or defection. Each node then interacts with its neighboring nodes in a prisoner's dilemma scenario, as defined by the payoffs T>R>P>S. The successful strategies then propagate across the network, replacing less successful strategies. The fraction of nodes that are cooperative is used as a metric. This experiment was conducted on many types of graphs, including small-world networks. Masuda and Aihara found that cooperation became dominant in small-world networks.

Once the original experiment has been implemented we plan to introduce a variant by altering the payoffs and strategies. We will use the snowdrift dilemma instead of the prisoner's dilemma. The snowdrift dilemma attempts to create a more realistic representation o the human interaction, by allowing strategies to be chosen with the ability to observe the actions of other players. The implementation of the snowdrift dilemma will be based on that used by Santos and Pacheco [3]. We believe that the fraction of strategies that are cooperative will be higher than in models that use the prisoner's dilemma.

A more ambitious extension would be to use automata for nodes instead on cooperate or defect. This would require the interaction between nodes to be an iterated prisoner's dilemma instead of the non-iterated version, as implemented in [The Further Evolution of Cooperation] by Axelrod and Douglas [4]. We could then observe which strategies became dominant. We suspect that TFT and other strategies that are known to be successful will be dominant in this model. Once this is implemented we could introduce an evolutionary component to the interactions between nodes. We would expect cooperative strategies to become dominant on small-world networks, and to find the correlation between the fraction of cooperative strategies found in the original experiment in each type of network and the degree to which cooperation evolved in the evolutionary model.


Our primary concern is that it may be difficult to interpret our results when we introduce more complicated interactions between nodes. In order to create a metric that may be compared to the original experiment we will need to find a way to measure how cooperative each strategy is. We will be able to measure the degree to which cooperation is present in different types of networks when the game being played on the networks is the same, but comparing the snowdrift dilemma to the prisoner's dilemma may prove challenging. We believe that it will be possible to compare the two, but we are concerned that our choice of a metric may affect our findings.




### Annotated Bibliography

[1] [**Spatial prisoner’s dilemma optimally played in small-world networks**](http://www.sciencedirect.com/science/article/pii/S0375960103006935#bBIB002)

Masuda, N., & Aihara, K. (2003). Spatial prisoner's dilemma optimally played in small-world networks. Physics Letters A, 313(1), 55-61.

Masuda and Aihara simulate an iterated prisoners dilemma with automata that interact only if they are connected on a graph. They simulate this on different types of networks, including regular graphs, lattices, and small-world networks. They find that small world networks produce cooperation to the greatest extent. They also investigate the effects of noise on the system, and consider the robustness of cooperation on the different networks.

[2] [**A simple rule for the evolution of cooperation on graphs**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2430087/)

Ohtsuki, H., Hauert, C., Lieberman, E., & Nowak, M. A. (2006). A simple rule for the evolution of cooperation on graphs. Nature, 441(7092), 502.

Ohtsuki, Hauert, Lieberman, and Nowak are motivated from that cooperation is the property of all biological system. They propose the simple graph model in which natural selection prefers cooperation in the certain condition. They assume vertice are divided into two types, cooperators who pay a cost for neighbors to receive a benefit and defectors who only receive benefits from cooperators. They simulate for various graph types(cycle, lattice, random regular graph, random graph and scale-free network) and find the condition that cooperators spread throughout the graph. They find that the fewer connections, the more cooperation in their model.


[3] [**Scale-free networks provide a unifying framework for the emergence of cooperation**](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.95.098104)

Santos, F. C., & Pacheco, J. M. (2005). Scale-free networks provide a unifying framework for the emergence of cooperation. Physical Review Letters, 95(9), 098104.

Santos and Pacheco find that cooperation becomes dominating features in scale-free networks, unlike regular graphs. They adopt the prisoner's dilemma and snowdrift game to research cooperation. As the correlation between individuals becomes bigger, the cooperation emerges throughout the entire population. They simulate the graph from small network with 100 individuals to very large population.


[4] [**The Further Evolution of Cooperation**](http://www.jstor.org/stable/1702320)

Axelrod, R., & Dion, D. (1988). The further evolution of cooperation. Science, 242(4884), 1385-1390.

Axelrod and Douglas argue that evolution can produce cooperation as a trait, even in situations where defection is a dominant strategy in a non-iterated version of the situation. They expand on the prisoner's dilemma tournament model used in Axelrods original tournament to incorporate evolutionary aspects. In the new model automata are constructed from a set of instructions, and then they interact with other automata as is the case in the older model. However, in addition to altering the population of each type of automata, the automata exchange instructions (chromosomes) or randomly alter a single instruction (mutation). Axelrod and Douglas conclude that cooperation can emerge from randomized evolution.
