import networkx
import numpy as np


class Node():
    C, D = 'C', 'D'
    T, R, P, S = 1, 0.25, 0, 0

    def __init__(self, state):
        """
        node object in graph. state is C or D
        """
        self.state = state
        self.score = 0  # will hold value calculated based on prisoners dilemma

    @classmethod
    def is_cooperator_state(cls, state):
        return state == cls.C

    def is_cooperator(self):
        return self.is_cooperator_state(self.state)

    def add_score(self, score):
        self.score += score

    def reset_score(self):
        self.score = 0

    # Play a single PD with neighbors, and calculate score
    #  neighbors: The list of Node object
    def play_pd(self, neighbors):
        """
        timestep for node
        """
        self.reset_score()
        for neighbor in neighbors:
            self.add_score(self.pd_score(neighbor.state))

    # play single PD
    def pd_score(self, neighbor_state):
        if self.is_cooperator():
            if self.is_cooperator_state(neighbor_state):
                return Node.R
            return Node.S
        else:
            if self.is_cooperator_state(neighbor_state):
                return Node.T
            return Node.P

    # Copy the state of the most successful neighbor
    def update_state(self, neighbors):
        max_score = max([neighbor.score for neighbor in neighbors])
        max_states = [neighbor.state for neighbor in neighbors if neighbor.score == max_score]
        self.state = max_states[0]

