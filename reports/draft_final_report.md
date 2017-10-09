### The Effect of Clustering on the Emergence of Cooperation in the Spatial Prisoner's Dilemma

Noah Rivkin, Changjun Lim

Abstract:

We attempted to reprodece and expand opun the findings of Masuda and Aihara[1]. Masuda and Aihara's work examines the spatial prisoners dilemma on small world graphs. They found that cooperative behavior emerged in a wide range of conditions. When we replicated their experiment we found qualitatively similar results, but under a smaller range of conditions. We also expanded on their original work by incorporating additional types of small world graphs. They had used only Watts-Strogatz[2] type graphs, while we tested Holmes-Kim graphs[3]. Masuda and Aihara suggest that their work may suggest why small-world networks are so prevalent in society. They also suggest that one reason why cooperation does not always dominate could be that the rewards for defection are too high. Our analysis suggests that their results do not hold under preferentialy attachment, which provides an additional explanation for real world examples where cooperation is not dominant.


Introduction:



-motivation



-methodology

-- what is the prisoners dilemma

-- types of graphs

-- implementation

Models and Results:

In order to validate our model we needed to show that it shared behavoir with Masuda and Aihara's[1] model. To do this, we tested what values of T lead to cooperation. In their work they used a rewired regular graph with n=3600 and k=8, and determined the percentage of the population that was cooperative for different values of T. A critical point was found at T=2.25 for p=0 and p=0.01. When we attempted to reproduce their results we found qualitative similarities, but a critical point of T=2 for p=0 and p=0.01. The transition region was 1.999<T<2, which is smaller than we expected. We also conducted the experiment using a 60 by 60 lattice. Masuda and Aihara found 4 distinct regimes, the last of which showed defection to be completely dominant after T=2.25. As before, our findings where qualitatively similar, but with only 3 regimes and lower values of T. 

## Insert Figure Here

We have been unable to determine the reason our results differ from the original experiments. Rewiring is not present when p=0, but our finding still vary. One possibility is that the initial distribution of cooperators is responsible. However, averaging the results over 10 trials makes this unlikely.



-Figure 2 explanation

-- description

-- figure with caption

-- reasoning/interpretation



-Expansion

-- description

-- figure with caption

-- reasoning/interpretation

Conclusions:

Annotated Bibliography:
