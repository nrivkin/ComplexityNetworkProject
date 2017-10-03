""" a crecreation of the spatial network thing
Noah Rivkin and Changjun Lim
"""

import networkx as nx
import numpy as np
from Spatialnet import SpatialNetwork
from PDnode import Node
import random

# It would be better to construct a class for

# TODO: create rules
n = 100  # the number of node
k = 8

# TODO: create node object
p = 0.9  # the initial ratio of cooperator
# initial state distribution(C/D) should be applied.

cooperators = random.sample(range(n), int(n * p))
nodes = [Node('C') if i in cooperators else Node('D') for i in range(n)]

G = SpatialNetwork(n, k, graph_type='regular')
Graph = G.G


# TODO: create main
def proceed_one_stage():
    # play a single PD
    for i in range(n):
        neighbor = [nodes[key] for key in Graph[i]]
        nodes[i].play_pd(neighbor)

    # update state
    for i in range(n):
        neighbor = [nodes[key] for key in Graph[i]]
        nodes[i].update_state(neighbor)

    c_ratio = len([node for node in nodes if node.is_cooperator()]) / n
    print("c ratio: {}".format(c_ratio))


# TODO: create test suite
N = 50  # the number of steps
for _ in range(N):
    proceed_one_stage()
