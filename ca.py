#!usr/bin/env python
import random
import numpy as np

from state import StateVector

class CA:

    def __init__(self, density, *, a, b):
        self.C = [[np.nan for _ in range(density.shape[1])] for _ in range(density.shape[0])]
        for i, row in enumerate(density):
            for j, col in enumerate(row):
                init_data = []
                x = 0
                for _ in range(a+b+2):
                    new_x = random.randint(0, col-x)
                    init_data.append(new_x)
                    x += new_x

                self.C[i][j] = StateVector(a, b, init_data=init_data)

    def nbhd(self, i: int, j: int):
        return self.C[i-1:i+2, j-1:j+2]

    def transition(self, i, j, neighbour):
        """ Transition function"""
        raise NotImplementedError()
