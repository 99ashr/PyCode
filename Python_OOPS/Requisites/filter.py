#!/usr/bin/env python3
#* ------------------------------ filter function ----------------------------- #

# & Syntax --> filter(function,iterables)
# ---------------------------------------------------------------------------- #
def func(i):
    if i >= 3:
        return i


x = list(filter(func, [2, 5, 8, 9, 1, 3, 0]))
print(x)

# ------------------- filter function using lambda function ------------------ #

x = list(filter(lambda a: a >= 3, [2, 5, 8, 9, 1, 3, 0]))
print(x)
# ---------------------------------------------------------------------------- #
#* ------------------------------------ EOF ----------------------------------- #
