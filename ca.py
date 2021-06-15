#!usr/bin/env python
from copy import deepcopy
import random

import numpy as np
import pygame
from state import StateVector


class CA:

    def __init__(self, density, *, a, b, cell_size, healthy_commuters=0.5, infected_commuters=0.1, long_distance_commuters=0.2):
        self.cell_size = cell_size
        self.density = density
        self.long_distance_commuters = long_distance_commuters
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
                    self.C[i][j] = StateVector(
                        a, b,
                        init_data=init_data,
                        h_commuters=healthy_commuters,
                        i_commuters=infected_commuters,
                        l_commuters=long_distance_commuters)
                else:
                    self.C[i][j] = col

    def nbhd(self, i: int, j: int):
        return self.C[i-1:i+2, j-1:j+2]

    @staticmethod
    def greater(matrix, n):
        results_x, results_y = list(), list()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > n:
                    results_x.append(i)
                    results_y.append(j)
        return results_x, results_y

    def run(self, n):
        dd = CA.greater(self.density, 3000)
        commuters_matrix = [[list()]*len(self.C[0])]*len(self.C)
        for _ in range(n):
            for i, row in enumerate(self.C):
                for j, col in enumerate(row):
                    if isinstance(col, StateVector):
                        nbhd_i = i+np.random.randint(-1, 1)
                        nbhd_j = j+np.random.randint(-1, 1)
                        min_dd_x = dd[0][0]
                        min_dd_y = dd[1][0]
                        min_dd = abs(i-dd[0][0]) + abs(j-dd[1][0])
                        for x, y in zip(dd[0], dd[1]):
                            if min_dd > abs(i-x) + abs(j-y):
                                min_dd = abs(i-x) + abs(j-y)
                                min_dd_x = x
                                min_dd_y = x

                        commuters = col.next(commuters_matrix)
                        commuters_nbhd, commuters_dd = deepcopy(commuters), deepcopy(commuters)
                        for state in commuters_nbhd:
                            state.n = state.n*(1-self.long_distance_commuters)
                        for state in commuters_dd:
                            state.n = state.n*self.long_distance_commuters

                        commuters_matrix[nbhd_i][nbhd_j].append(commuters_nbhd)
                        commuters_matrix[min_dd_x][min_dd_y].append(commuters_dd)

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
