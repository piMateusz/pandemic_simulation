#!usr/bin/env python
import random
import numpy as np

class State:

    def __init__(self, n: int, type: str, day=0):
        if type in ['S', 'E', 'I', 'R']:
            self.type = type
        else:
            raise ValueError('Invalid type value. Choose from [S, E, I, R]')
        self._day = day
        if n >= 0:
            self.n = n
        else:
            raise ValueError("Number must be positive")

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, _):
        raise TypeError("Day can't be changed")

    def __repr__(self):
        return f"State ({self.type}, {self.day}, {self.n})"

class StateVector:
    __key_map = None

    def __init__(self, a, b, init_data=None):
        self.a = a
        self.b = b
        if init_data:
            if len(init_data) == a+b+2:
                self.__vector = [
                    State(init_data[0], 'S'),
                    *(State(n, 'E', day=i) for i, n in enumerate(init_data[1:a+1])),
                    *(State(n, 'I', day=i) for i, n in enumerate(init_data[a+1:a+b+1])),
                    State(init_data[-1], 'R')
                ]
            else:
                raise ValueError('Init data length must be equal a+b+2')
        else:
            self.__vector = [
                State(0, 'S'),
                *(State(0, 'E', day=i) for i in range(a)),
                *(State(0, 'I', day=i) for i in range(a)),
                State(0, 'R')
            ]
        StateVector.__key_map = {
            "S": 0,
            **{f"E{i}": i for i in range(1, self.a+1)},
            **{f"I{i}": i for i in range(self.a, self.a+self.b+1)},
            "R": 0
        }

    def __len__(self):
        return self.a+self.b+2

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__vector[key]
        elif key in StateVector.key_map:
            return self.__vector[StateVector.__key_map[key]]
        else:
            raise KeyError('Key must be int or proper string')

    def __setitem__(self, key: int, value):
        self.__vector[key].n = value

    def __repr__(self):
        return f"{self.__vector}"

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
