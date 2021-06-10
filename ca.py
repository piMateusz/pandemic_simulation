#!usr/bin/env python
import random
import numpy as np
import pygame
from state import StateVector
import sys
np.set_printoptions(threshold=sys.maxsize)


class CA:

    def __init__(self, density, *, a, b, cell_size):
        self.cell_size = cell_size
        self.C = [[np.nan for _ in range(density.shape[1])] for _ in range(density.shape[0])]
        for i, row in enumerate(density):
            for j, col in enumerate(row):
                if not np.isnan(col):
                    init_data = []
                    x = 0
                    for _ in range(a+b+2):
                        new_x = random.randint(0, int(col)-x)
                        init_data.append(new_x)
                        x += new_x

                    self.C[i][j] = StateVector(a, b, init_data=init_data)
                else:
                    self.C[i][j] = col

    def nbhd(self, i: int, j: int):
        return self.C[i-1:i+2, j-1:j+2]

    def draw_infected(self, win):
        infected_matrix = np.zeros((len(self.C), len(self.C[0])))
        for x, row in enumerate(self.C):
            for y, state_vector in enumerate(row):
                if isinstance(state_vector, StateVector):
                    all_infected = 0
                    for i in range(1, state_vector.a + 1):
                        all_infected += state_vector[f"E{i}"].n
                    infected_matrix[x, y] = all_infected
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
                    pygame.draw.rect(win, (0, 0, 255),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def draw_density_map(self, win):
        pass

    def transition(self, i, j, neighbour):
        """ Transition function"""
        raise NotImplementedError()