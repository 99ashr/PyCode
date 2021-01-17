#!/usr/bin/env python3

#* ------------------------------ Numpy v/s List ------------------------------ #
# ! Numpy is fast, consumes low memory and convenient to use over list.

import numpy as np
import sys

#? -------------------------------- List-Memory ------------------------------- #

list = range(1000)
print("Memory of elements of List:", sys.getsizeof(1)*len(list))
# ---------------------------------------------------------------------------- #

#? ------------------------------- Numpy-Memory ------------------------------- #
d = np.arange(1000)
print("Memory size of elements of an array using numpy: ", d.size*d.itemsize)
# ---------------------------------------------------------------------------- #

#* ------------------------------------ EOF ----------------------------------- #
