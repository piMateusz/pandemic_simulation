#!usr/bin/env python
import random

import numpy as np

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
