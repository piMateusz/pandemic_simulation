#!usr/bin/env python
import numpy as np
import read
from pandemic_simulation import main

if __name__ == '__main__':
    polmap = read.read_asc("data/polds00g.asc")
    # sample = np.array([[10, 10, 10], [10, 10, 10]])
    # sample1 = np.array([[100]])
    main()
    # x = np.array([0, 100, 1])
    # print(np.where(polmap > 3000))
    # print(polmap[68, 243])
