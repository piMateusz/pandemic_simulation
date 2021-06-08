#!usr/bin/env python
from constants import BIRTH_DEATH_RATE as MU

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

    def __init__(self, a, b, init_data=None, beta=1):
        self.a = a
        self.b = b
        self.beta = beta
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
            **{f"I{i}": i for i in range(self.a+1, self.a+self.b+1)},
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

    def total(self, type='all'):
        types = {
            "all": self.__vector,
            "S": self.__vector[0],
            "E": self.__vector[1:self.a+1],
            "I": self.__vector[self.a+1:self.a+self.b+1],
            "R": self.__vector[-1]
        }
        if type not in types:
            raise ValueError("Invalid type. Choose from  [all, S, E, I, R]")
        return sum((state.n for state in types.get(type)))

    def _dS(self):
        s = self.total('S')
        i = self.total('I')
        n = self.total()
        return MU*(n-s) - self.beta*(i/n)*s

    def _dE(self):
        s = self.total('S')
        i = self.total('I')
        n = self.total()
        e = self.total('E')
        return self.beta*(i/n)*s - (MU+1/self.a)*e

    def _dI(self):
        e = self.total('E')
        i = self.total('I')
        return 1/self.a*e - (MU + 1/self.a)*i

    def _dR(self):
        i = self.total('I')
        r = self.total('R')
        return (1/self.a)*i - MU*r

    def next(self):
        for it in range(1, self.a):
            self.__vector[it+1].n = self.__vector[it].n
        for it in range(self.a+1, self.a+self.b):
            self.__vector[it+1].n = self.__vector[it].n
        #TODO add derivatives
