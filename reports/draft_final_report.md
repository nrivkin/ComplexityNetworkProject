### The Effect of Clustering on the Emergence of Cooperation in the Spatial Prisoner's Dilemma

Noah Rivkin, Changjun Lim

Abstract:

We attempted to reprodece and expand upon the findings of Masuda and Aihara[1]. Masuda and Aihara's work examines the spatial prisoners dilemma on small world graphs. They found that cooperative behavior emerged in a wide range of conditions. When we replicated their experiment we found qualitatively similar results, but under a smaller range of conditions. We also expanded on their original work by incorporating additional types of small world graphs. They had used only Watts-Strogatz[2] type graphs, while we tested Holmes-Kim graphs[3]. Masuda and Aihara suggest that their work may suggest why small-world networks are so prevalent in society. They also suggest that one reason why cooperation does not always dominate could be that the rewards for defection are too high. Our analysis suggests that their results do not hold under preferentialy attachment, which provides an additional explanation for real world examples where cooperation is not dominant.


Introduction:



-motivation



-methodology

-- what is the prisoners dilemma

-- types of graphs

-- implementation

Models and Results:

In order to validate our model we needed to show that it shared behavior with Masuda and Aihara's[1] model. To do this, we tested what values of T lead to cooperation. In their work they used a rewired regular graph with n=3600 and k=8, and determined the percentage of the population that was cooperative for different values of T. A critical point was found at T=2.25 for p=0 and p=0.01. When we attempted to reproduce their results we found qualitative similarities, but a critical point of T=2 for p=0 and p=0.01. The transition region was 1.999<T<2, which is smaller than we expected. We also conducted the experiment using a 60 by 60 lattice. Masuda and Aihara found 4 distinct regimes, the last of which showed defection to be completely dominant after T=2.25. As before, our findings where qualitatively similar, but with only 3 regimes and lower values of T. 

## Insert Figure Here

We have been unable to determine the reason our results differ from the original experiments. Rewiring is not present when p=0, but our finding still vary. One possibility is that the initial distribution of cooperators is responsible. However, averaging the results over 10 trials makes this unlikely.


 
 In the first experiment, we observed that there are 3 regimes after stabilization. In the second regime, the proportion of cooperators decreases as rewiring parameter p increases, that is, clustering coefficient decreases. We draw the proportion of cooperator over time graph to check the tendency of the network over time. We simulate it by giving 3 values of b and c(0) pair and changing p value with 0, 0.001, 0.01, 0.1, and 0.8, the initial ratio of cooperators. We set the first condition for Fig 2.(a) and (d) as b = 1.1 and c(0) = 0.1 because cooperators are dominant in the first regime. The second condition for Fig 2.(b) and (e) is b = 1.7 and c(0) = 0.5. The third condition for Fig 2.(c) and (f) is b = 3 and c(0) = 0.995 since defectors are dominant.
 
 Unlike Masuda and Aihara obseved that cooperators dominate defector in the first condition, the proportions of cooperators converge to 0 in almost condition and the proportion of cooperators after transient increases when p is large in Fig. 2(a). If a cooperator is among defects, it will always get less gain than defectors. So cooperators should be clusterred at the beginning in order to dominate. However, cooperators are surrounded by defectors under the low initial condition so defectors dominate.
 
 논문에서 저자가 확인한 실험에서는 첫번째 조건에서 항상 cooperator 비율이 거의 100%에 수렴한 반면에, 우리가 한 실험에서는 거의 대부분의 조건에서 0으로 수렴하였고, 오히려 p가 클 때 cooperator 비율이 높아졌다. 앞선 결과에서 한 예측과 일부 달랐다. cooperator가 defect 사이에 있으면, defector에 비해 얻는 이득이 항상 적기 때문에, cooperator가 우세하기 위해서는 초기에 cooperator가 서로 clustering 된 상황에 놓여있어야 한다. 하지만 낮은 초기조건에서는 cooperator가 clustering을 형성할 가능성이 적기 때문에 defector로 둘러싸여있게 된다. cooperator가 수렴하는 것으로 보인다.


세번쩨 조건에서는 예상처럼 cooperator는 모두 0으로 수렴하였다. cooperator가 감소하는 속도는 p에 따라 달라졌다. 우리가 예측한 결과대로 p가 클수록 더 빠르게 감소하였다. p가 클수록 path length가 짧아져서 더 빨리 전파되는 것으로 볼 수 있다.

-- figure with caption

![figure2_a](images/fig2_a.png)

![figure2_b](images/fig2_b.png)

![figure2_c](images/fig2_c.png)

![figure2_d](images/fig2_d.png)

![figure2_e](images/fig2_e.png)

![figure2_f](images/fig2_f.png)

-- reasoning/interpretation



-Expansion

-- description

-- figure with caption

-- reasoning/interpretation

Conclusions:


### Annotated Bibliography:

[1] [**Spatial prisoner’s dilemma optimally played in small-world networks**](http://www.sciencedirect.com/science/article/pii/S0375960103006935#bBIB002)

Masuda, N., & Aihara, K. (2003). Spatial prisoner's dilemma optimally played in small-world networks. Physics Letters A, 313(1), 55-61.

Masuda and Aihara simulate an iterated prisoners dilemma with automata that interact only if they are connected on a graph. They simulate this on different types of networks, including regular graphs, lattices, and small-world networks. They find that small world networks produce cooperation to the greatest extent. They also investigate the effects of noise on the system, and consider the robustness of cooperation on the different networks.