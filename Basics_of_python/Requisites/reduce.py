#!/usr/bin/env python3
#* ------------------------------ Reduce Function ----------------------------- #
# & Syntax --> reduce(function,iterables)
# ! reduce function applies the given function and return a single value.
# ---------------------------------------------------------------------------- #
from functools import reduce
lst = [2, 4, 6, 8]
x = reduce(lambda a, b: a+b, lst)
print(x)
#* ------------------------------------ EOF ----------------------------------- #
