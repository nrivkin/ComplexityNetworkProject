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
n = 3600  # the number of node
k = 8

# TODO: create node object
p = 0.98  # the initial ratio of cooperator
# initial state distribution(C/D) should be applied.

cooperators = random.sample(range(n), int(n * p))
nodes = [Node('C') if i in cooperators else Node('D') for i in range(n)]

G = SpatialNetwork(n, k, graph_type='lattice')
Graph = G.G


class TestBench:
    def __init__(self, n, k, graph_type, c0, p=None, N=100, M=10):
        self.n = n  # the number of nodes
        self.graph = SpatialNetwork(n, k, graph_type, dep=p).G
        self.c0 = c0  # initial cooperator ratio
        self.N = N  # the number of steps
        self.M = M  # the number of test
        self.ratio = list()
        self.nodes = list()
        self.initialize()

    def initialize(self):
        cooperators = random.sample(range(self.n), int(self.n * self.c0))
        self.nodes = [Node('C') if i in cooperators else Node('D') for i in range(self.n)]
        self.ratio = list()

    def step(self):
        # play a single PD
        for i in range(self.n):
            neighbor = [self.nodes[key] for key in self.graph[i]]
            self.nodes[i].play_pd(neighbor)

        # get the highest neighbors' state
        for i in range(self.n):
            neighbor = [self.nodes[key] for key in self.graph[i]]
            self.nodes[i].get_max_state(neighbor)

        # update the state
        for i in range(self.n):
            self.nodes[i].update_state()

        c_ratio = len([node for node in self.nodes if node.is_cooperator()]) / self.n
        self.ratio.append(c_ratio)

    def iterate(self):
        ratios = np.zeros((self.M, self.N))
        for i in range(self.M):
            self.initialize()
            for _ in range(self.N):
                self.step()
            ratios[i] = self.ratio
        self.ratio = np.average(ratios, axis=0)

    def draw(self):
        x = range(1, len(self.ratio) + 1)
        plt.plot(x, self.ratio * 100)
        plt.xlabel('time')
        plt.ylabel('% C')
        plt.ylim(0, 100)
        plt.show()


def time_ratio_graph(n, k, graph_type, c0, N, p=None, M=10, T=1, R=0.25, P=0, S=0):
    Node.change_rule(T, R, P, S)
    bench = TestBench(n, k, graph_type, c0, p, N, M)
    bench.iterate()
    bench.draw()