#!/usr/bin/env python3

#* -------------------- Filter function within Map function ------------------- #
# ---------------------------------------------------------------------------- #

from functools import reduce
x = list(map(lambda a: a+a, filter(lambda a: a >= 3, [1, 2, 3, 4])))
print("Filter function within Map function", x)

# ---------------------------------------------------------------------------- #

#* -------------------- Map function within Filter function ------------------- #
# ---------------------------------------------------------------------------- #

y = list(filter(lambda a: a >= 3, map(lambda a: a+a, [1, 2, 3, 4])))
print("Map function within filter function", y)

# ---------------------------------------------------------------------------- #

#* --------------- Map and Filter function with reduce function --------------- #
# ---------------------------------------------------------------------------- #
r = reduce(lambda a, b: a+b, filter(lambda a: a >=
                                    3, map(lambda a: a+a, [1, 2, 3, 4])))
print("Map and Filter function within reduce function", r)

#* ------------------------------------ EOF ----------------------------------- #
