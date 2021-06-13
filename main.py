#!usr/bin/env python
import numpy as np
import ca
import read

if __name__ == '__main__':
    polmap = read.read_asc("data/polds00g.asc")
    sample = np.array([[10, 10, 10], [10, 10, 10]])
    sample1 = np.array([[100]])

    cell_auto = ca.CA(sample1, a=2, b=2)
    cell_auto.run(4)
