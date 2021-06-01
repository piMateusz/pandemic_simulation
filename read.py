#!/usr/bin/env python

import re
import numpy as np

def read_asc(file, delimiter=" "):
    is_ncols = is_nrows = is_xll = is_yll = is_cellsize = is_nodata = False
    data = None
    with open(file) as fp:
        for it, line in enumerate(fp.readlines()):
            if all((is_nrows, is_ncols, is_xll, is_yll, is_cellsize, is_nodata)):
                if data is None:
                    data = np.zeros((nrows, ncols))
                data[it-6, :] = np.array([float(x) if x != nan else np.nan for x in line.split(delimiter)[:-1]])
            elif it > 6:
                raise TypeError("File is not an asc file")

            if re.match(r"ncols", line):
                ncols = int(re.split(r"\s+", line)[1])
                is_ncols = True
            if re.match(r"nrows", line):
                nrows = int(re.split(r"\s+", line)[1])
                is_nrows = True
            if re.match(r"xllcorner", line):
                is_xll = True
            if re.match(r"yllcorner", line):
                is_yll = True
            if re.match(r"cellsize", line):
                is_cellsize = True
            if re.match(r"NODATA_value", line):
                nan = re.split(r"\s+", line)[1]
                is_nodata = True
        return data
