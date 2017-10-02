import networkx as nx
import numpy as np


class SpatialNetwork():
    def __init__(self, n, k, graph_type='regular', dep = None, snowdrift=False):
        """creates spatial network"""
        self.n = n
        self.k = k
        self.dep = dep
        G = create_graph(self, graph_type)
        self.G = G

    def create_graph(self, graph_type):
        if graph_type == 'lattice':
            return self.create_lattice()
        elif graph_type == 'WS':
            return nx.powerlaw_cluster_graph(4039, 22, 0)
        elif graph_type == 'HK':
            if self.dep != None:
                return nx.powerlaw_cluster_graph(self.n, self.k, self.dep)
            else:
                return nx.powerlaw_cluster_graph(self.n, self.k, .3)
        G = self.create_regular()
        if graph_type == 'regular':
            return G
        elif graph_type == 'ER':
            return self.rewire(G, p=.3)
        elif graph_type == 'random':
            return self.rewire(G, p=1)
        else:
            raise ValueError('not a recognized graph type')

    def create_regular(self):
        """
        creates regular graph. Is a helper function for rewired graphs. Some
        code taken from/based on jupyter notebook chap3, credit to Allen Downey
        """
        G = nx.DiGraph()
        quo, rem = divmod(self.k, 2)
        nodes = list(range(self.n))
        G.add_nodes_from(nodes)
        G.add_edges_from(adjacent_edges(nodes, quo))
        # if k is odd, add opposite edges
        if rem:
            if n%2:
                msg = "Can't make a regular graph if n and k are odd."
                raise ValueError(msg)
            G.add_edges_from(opposite_edges())
        return G

    def create_lattice(self):
        """
        creates a lattice graph with n nodes that is k long
        """
        G = nx.DiGraph()
        nodes = list(range(self.n))
        G.add_nodes_from(nodes)
        for node in nodes:
            if node + self.k in nodes:
                G.add_edge(node, node + self.k)
            if node % self.k != 0 and node + 1 in nodes:
                G.add_edge(node, node + 1)
        return G

    def rewire(self, G, p):
        """Rewires each edge with probability `p`.
        code taken from/based on jupyter notebook chap3, credit to Allen Downey
        G: Graph
        p: float
        """
        if self.dep != None:
            p = self.dep
        nodes = set(G.nodes())
        for edge in G.edges():
            if flip(p):
                u, v = edge
                choices = nodes - {u} - set(G[u])
                new_v = np.random.choice(tuple(choices))
                G.remove_edge(u, v)
                G.add_edge(u, new_v)
        return G

def adjacent_edges(nodes, halfk):
    """
    code taken from/based on jupyter notebook chap3, credit to Allen Downey
    """
    n = len(nodes)
    for i, u in enumerate(nodes):
        for j in range(i+1, i+halfk+1):
            v = nodes[j % n]
            yield u, v

def opposite_edges(nodes):
    """Enumerates edges that connect opposite nodes.
    code taken from/based on jupyter notebook chap3, credit to Allen Downey
    """
    n = len(nodes)
    for i, u in enumerate(nodes):
        j = i + n//2
        v = nodes[j % n]
        yield u, v

def flip(p):
    """Returns True with probability `p`."""
    return np.random.random() < p

# for testing
# net = SpatialNetwork(10,4,graph_type='HK')
# 
# # colors from our friends at http://colorbrewer2.org
# COLORS = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462',
#           '#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5','#ffed6f']
# 
# nx.draw_circular(net.G,
#                  node_color=COLORS[0],
#                  node_size=2000,
#                  with_labels=True)