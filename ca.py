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
                for it in range(3):
                    while True:
                        new_x = random.randint(0, col-x)
                        if it or new_x:
                            break
                    init_data.append(new_x)
                    x += new_x

                self.C[i][j] = StateVector(a, b, init_data=init_data)

    def nbhd(self, i: int, j: int):
        return self.C[i-1:i+2, j-1:j+2]

    def run(self, n):
        for _ in range(n):
            for row in self.C:
                for col in row:
                    col.next()
