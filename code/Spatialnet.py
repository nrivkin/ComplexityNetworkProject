import networkx as nx
import numpy as np


<<<<<<< HEAD
class SpatialNetwork():
    def __init__(self, n, k, graph_type='regular', dep = None, snowdrift=False):
        """creates spatial network"""
        self.n = n
        self.k = k
        if dep != None:
            self.dep = dep
        G = create_graph(self, graph_type)
        self.G = G

    def create_graph(self, graph_type):
        G = create_regular(self)
        if type == 'regular':
            return G
        elif type == 'smallworld':
            return rewire(G, p=.3)
        elif type == 'random':
            return rewire(G, p=1)
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
        node_data = [n for n in nodes] # will eventually add Node()
        G.add_nodes_from(nodes)
        print(G.nodes)
        G.add_edges_from(adjacent_edges(G.nodes(), quo))
        # if k is odd, add opposite edges
        if rem:
            if n%2:
                msg = "Can't make a regular graph if n and k are odd."
                raise ValueError(msg)
            G.add_edges_from(opposite_edges())
        return G

    def rewire(G, p):
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
                new_v = choice(tuple(choices))
                G.remove_edge(u, v)
                G.add_edge(u, new_v)

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
net = SpatialNetwork(10,4)
net

