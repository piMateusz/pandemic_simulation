#!usr/bin/env python
import random

import numpy as np
import pygame
from state import StateVector


class CA:

    def __init__(self, density, *, a, b, cell_size):
        self.cell_size = cell_size
        self.C = [[np.nan for _ in range(density.shape[1])] for _ in range(density.shape[0])]
        for i, row in enumerate(density):
            for j, col in enumerate(row):
                if not np.isnan(col):
                    init_data = []
                    x = 0
                    for it in range(3):
                        while True:
                            new_x = random.randint(0, int(col)-x)
                            if it or new_x:
                                break
                        init_data.append(new_x)
                        x += new_x
                    self.C[i][j] = StateVector(a, b, init_data=init_data)
                else:
                    self.C[i][j] = col

    def nbhd(self, i: int, j: int):
        return self.C[i-1:i+2, j-1:j+2]

    def run(self, n):
        for _ in range(n):
            for row in self.C:
                for col in row:
                    if isinstance(col, StateVector):
                        col.next()

    def draw_infected(self, win):
        infected_matrix = np.zeros((len(self.C), len(self.C[0])))
        for x, row in enumerate(self.C):
            for y, state_vector in enumerate(row):
                if isinstance(state_vector, StateVector):
                    infected_matrix[x, y] = state_vector.total('E')
                else:
                    infected_matrix[x, y] = -1
        # normalize to grayscale
        infected_max = np.max(infected_matrix)
        infected_matrix = infected_matrix * 255 // infected_max

        for y in range(infected_matrix.shape[0]):
            for x in range(infected_matrix.shape[1]):
                if infected_matrix[y, x] != -1:
                    pygame.draw.rect(win, (infected_matrix[y, x], infected_matrix[y, x], infected_matrix[y, x]),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(win, (0, 0, 128),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
