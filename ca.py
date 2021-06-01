#!usr/bin/env python
import random

import numpy as np

class State:
    S = 0
    E = 1
    I = 2
    R = 3

    def __init__(self, density):
        self.population = random.choices([State.S, State.E, State.I, State.R], k=density)

    def __repr__(self):
        return f"State ({self.population})"

class CA:

    def __init__(self, density):
        self.C = [[np.nan for _ in range(density.shape[1])] for _ in range(density.shape[0])]
        for i, row in enumerate(density):
            for j, col in enumerate(row):
                self.C[i][j] = State(col)

        print(self.C)

    def nbhd(self, i, j):
        return self.C[i-1:i+2, j-1:j+2]

    def transition(self, i, j, neighbour):
        """ Transition function"""
        raise NotImplementedError()
