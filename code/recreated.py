import random
import matplotlib.pyplot as plt
import numpy as np
from PDnode import Node
from Spatialnet import SpatialNetwork


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
        self.nodes = [Node(Node.C) if i in cooperators else Node(Node.D) for i in range(self.n)]
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

    def draw2(self, label=None):
        ratio = np.insert(self.ratio, 0, self.c0)
        x = range(len(ratio))
        if label is None:
            plt.plot(x, ratio * 100)
        else:
            plt.plot(x, ratio * 100, label=label)
            plt.xlabel('time')
            plt.ylabel('% C')


def time_ratio_graph(n, k, graph_type, c0, N, p=None, M=10, T=1, R=0.25, P=0, S=0):
    Node.change_rule(T, R, P, S)
    bench = TestBench(n, k, graph_type, c0, p, N, M)
    bench.iterate()
    bench.draw()


def T_ratio_graph(n, k, graph_type, c0, N=100, p=None, M=10, T_min=1, T_max=2.5, T_steps=16, R=1, P=0, S=0):
    ratios = []
    T_values = []
    for T in np.linspace(T_min, T_max, T_steps):
        Node.change_rule(T, R, P, S)
        bench = TestBench(n, k, graph_type, c0, p, N, M)
        bench.iterate()
        ratios.append((bench.ratio[len(bench.ratio) - 1] * 100))
        T_values.append(T)
    plt.plot(T_values, ratios)
    plt.xlabel('T')
    plt.ylabel('% C')
    plt.ylim(0, 100)
    plt.show()


def time_ratio_rewire_graph(n, k, graph_type, c0, N, M=10, T=1, R=0.25, P=0, S=0):
    Node.change_rule(T, R, P, S)
    if graph_type == 'WS':
        gt = 'regular'
    elif graph_type == 'rewired_lattice':
        gt = 'lattice'
    else:
        gt = graph_type
    bench = TestBench(n=n, k=k, graph_type=gt, c0=c0, N=N, M=M)
    bench.iterate()
    bench.draw2("p=0")
    ps = [0.001, 0.01, 0.1, 0.8]
    for p in ps:
        bench = TestBench(n, k, graph_type, c0, p, N, M)
        bench.iterate()
        bench.draw2("p=" + str(p))
    plt.legend()
    plt.show()
