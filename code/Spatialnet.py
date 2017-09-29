import networkx
import numpy as np


class Network():
    def __init__(self, n, k, type='smallworld'):
        G = self.create_graph(n, k, type)
        self.G = G

    def create_graph(self, n, k, type):
        if type == 'smallworld':
            pass
        elif type == 'regular':
            pass
        elif type == 'random':
            pass
        else:
            raise ValueError('not a recognized graph type')
