#!usr/bin/env python
from copy import deepcopy
import numpy as np
import sys

import constants

class State:

    def __init__(self, n: int, type_: str, day=0):
        if type_ in ['S', 'E', 'I', 'R']:
            self.type = type_
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

    def __init__(self, a, b, h_commuters, i_commuters, l_commuters, init_data=None, beta=1):
        self.a = a
        self.b = b
        self.beta = beta
        self.h_commuters = h_commuters
        self.i_commuters = i_commuters
        self.l_commuters = l_commuters
        if init_data:
            if len(init_data) == 3:
                self.__vector = [
                    State(init_data[0], 'S'),
                    *(State(n, 'E', day=i) for i, n in enumerate([init_data[1]]+[0]*(a-1))),
                    *(State(n, 'I', day=i) for i, n in enumerate([init_data[2]]+[0]*(b-1))),
                    State(init_data[-1], 'R')
                ]
            else:
                raise ValueError('Init data length must equal 3')
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
        elif key in StateVector.__key_map:
            return self.__vector[StateVector.__key_map[key]]
        else:
            raise KeyError('Key must be int or proper string')

    def __setitem__(self, key: int, value):
        self.__vector[key].n = value

    def __repr__(self):
        return f"{self.__vector}"

    def _infection_prob(self):
        if self.total() == 0:
            return 0
        q = np.random.normal(1-np.exp(-self.beta*(self.total('I')/self.total())))
        if q < 0:
            return 0
        if q > 1:
            return 1
        return q

    def total(self, type_='all'):
        types = {
            "all": self.__vector,
            "S": self.__vector[0:1],
            "E": self.__vector[1:self.a+1],
            "I": self.__vector[self.a+1:self.a+self.b+1],
            "R": self.__vector[-1:]
        }
        if type_ not in types:
            raise ValueError("Invalid type. Choose from  [all, S, E, I, R]")
        return sum((state.n for state in types.get(type_)))

    def commuters(self):
        commuters_v = deepcopy(self.__vector)
        commuters_v[0].n = self.__vector[0].n*self.h_commuters
        for it in range(1, self.a+self.b+1):
            commuters_v[it].n = self.__vector[it].n*self.i_commuters
        commuters_v[-1].n = self.__vector[-1].n*self.h_commuters
        return commuters_v

    def _dS(self, prev, prob, commuters_in, commuters_out):
        if commuters_in:
            n = sum((vect[0].n for vect in commuters_in))
        else:
            n = 0
        return round((1-constants.DEATH+constants.BIRTH)*\
            ((1-prob)*(prev[0].n-commuters_out[0].n)+(1-prob)*n))

    def _dE(self, prev, prob, it, commuters_in, commuters_out):
        if self.__vector[it].day == 0:
            if commuters_in:
                n = sum((vect[0].n for vect in commuters_in))
            else:
                n = 0
            return round((1-constants.DEATH+constants.BIRTH)*\
                (prob*(prev[0].n-commuters_out[0].n)+prob*n))
        return round((1-constants.DEATH+constants.BIRTH-constants.MORTALITY)*prev[it-1].n)

    def _dI(self, prev, it):
        if self.__vector[it].day == 0:
            return round((1-constants.DEATH+constants.BIRTH-constants.MORTALITY)*prev[self.a].n)
        return round((1-constants.DEATH+constants.BIRTH-constants.MORTALITY)*prev[it-1].n)

    def _dR(self, prev):
        return round((1-constants.DEATH-constants.BIRTH)*prev[-1].n+\
            (1-constants.DEATH+constants.BIRTH-constants.MORTALITY)*\
            prev[-2].n)

    def next(self, commuters_in):
        #TODO: Dodaj dane z commuters do wyliczania pochodnych str 5, (18)-(23)
        commuters_out = self.commuters()
        inf_prob = self._infection_prob()
        vect = deepcopy(self.__vector)
        self.__vector[0].n = self._dS(vect, inf_prob, commuters_in, commuters_out)
        for it in range(1, self.a+1):
            self.__vector[it].n = self._dE(vect, inf_prob, it, commuters_in, commuters_out)
        for it in range(self.a+1, self.a+self.b+1):
            self.__vector[it].n = self._dI(vect, it)
        self.__vector[-1].n = self._dR(vect)
        return commuters_out
