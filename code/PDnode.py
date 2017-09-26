import networkx
import numpy as np
import Spatialnet

class Node():
    def __init__(self, state):
        """
        node object in graph. state is C or D
        """
        # TODO: make function
        self.state = state
        self.score # will hold value calculated based on prisoners dilemma
        pass

    def update(self, neighbors):
        """
        timestep for node
        """
        # TODO: timestep
        pass
