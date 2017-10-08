import networkx as nx
import numpy as np
import random


class SpatialNetwork():
    def __init__(self, n, k, graph_type='regular', dep=None, snowdrift=False):
        """creates spatial network"""
        self.n = n
        self.k = k
        self.dep = dep
        self.G = self.create_graph(graph_type)

    def create_graph(self, graph_type):
        if graph_type == 'lattice':
            return self.create_lattice()
        if graph_type == 'rewired_lattice':
            G = self.create_lattice()
            return self.rewire(G, p=.3, k=4)
        elif graph_type == 'powerlaw':
            return nx.powerlaw_cluster_graph(self.n, self.k, 0)
        elif graph_type == 'HK':
            if self.dep != None:
                return nx.powerlaw_cluster_graph(self.n, self.k, self.dep)
            else:
                return nx.powerlaw_cluster_graph(self.n, self.k, .3)
        G = self.create_regular()
        if graph_type == 'regular':
            return G
        elif graph_type == 'WS':
            return self.rewire(G, p=.3, k=self.k)
        elif graph_type == 'random':
            return self.rewire(G, p=1, k=self.k)
        else:
            raise ValueError('not a recognized graph type')

    def create_regular(self):
        """
        creates regular graph. Is a helper function for rewired graphs. Some
        code taken from/based on jupyter notebook chap3, credit to Allen Downey
        """
        G = nx.Graph()
        quo, rem = divmod(self.k, 2)
        nodes = list(range(self.n))
        G.add_nodes_from(nodes)
        G.add_edges_from(adjacent_edges(nodes, quo))
        # if k is odd, add opposite edges
        if rem:
            if self.n % 2:
                msg = "Can't make a regular graph if n and k are odd."
                raise ValueError(msg)
            G.add_edges_from(opposite_edges())
        return G

    def create_lattice(self):
        """
        creates a lattice graph with n nodes that is k long
        """
        G = nx.Graph()
        nodes = list(range(self.n))
        G.add_nodes_from(nodes)
        for node in nodes:
            if node + self.k in nodes:
                G.add_edge(node, node + self.k)
            if node % self.k != (self.k - 1) and node + 1 in nodes:
                G.add_edge(node, node + 1)
        return G

    def rewire(self, G, p, k):
        """Rewires each edge with probability `p`.
        code taken from/based on jupyter notebook chap3, credit to Allen Downey
        G: Graph
        p: float
        """
        if self.dep != None:
            p = self.dep
        rewire_num = p * k * self.n / 2
        all_edges = list(G.edges)
        np.random.shuffle(all_edges)
        chosen = all_edges[0:int(rewire_num - .5)]
        G.remove_edges_from(chosen)
        need_replace = set([node for node in list(G.nodes()) if len(list(G.neighbors(node))) < k])
        while len(need_replace) > 1:
            start = random.choice(tuple(need_replace))
            found = False
            pos1 = ()
            for node in need_replace:
                if not found:
                    pos1 = (start, node)
                    pos2 = (node, start)
                    if start != node and pos1 not in G.edges and pos2 not in G.edges and pos1 not in chosen \
                            and pos2 not in chosen:
                        found = True
                        G.add_edge(start, node)
            if found == False:
                need_replace.remove(start)
            need_replace = need_replace - set([node for node in pos1 if len(list(G.neighbors(node))) >= k])
        return G


def adjacent_edges(nodes, halfk):
    """
    code taken from/based on jupyter notebook chap3, credit to Allen Downey
    """
    n = len(nodes)
    for i, u in enumerate(nodes):
        for j in range(i + 1, i + halfk + 1):
            v = nodes[j % n]
            yield u, v


def opposite_edges(nodes):
    """Enumerates edges that connect opposite nodes.
    code taken from/based on jupyter notebook chap3, credit to Allen Downey
    """
    n = len(nodes)
    for i, u in enumerate(nodes):
        j = i + n // 2
        v = nodes[j % n]
        yield u, v