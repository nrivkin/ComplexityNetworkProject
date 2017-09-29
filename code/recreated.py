""" a crecreation of the spatial network thing
Noah Rivkin and Changjun Lim
"""

import networkx as nx
import numpy as np
from code.Spatialnet import Network
from code.PDnode import Node

# It would be better to construct a class for

# TODO: create rules
n = 100
k = 8

# TODO: create node object
# initial state distribution(C/D) should be applied.
nodes = [Node('C') for i in range(n)]

Graph = Network(n, k)


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

# TODO: create test suite