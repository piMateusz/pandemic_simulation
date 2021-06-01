#!usr/bin/env python
import numpy as np
import ca
import read

if __name__ == '__main__':
    polmap = read.read_asc("data/polds00g.asc")
    sample = np.array([[1, 2, 3], [1, 2, 3]])

    ca.CA(sample)