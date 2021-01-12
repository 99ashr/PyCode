#!/usr/bin/env python3

#* -------------------------------- Generators -------------------------------- #
#! Generators return traversable objects, that too one at a time. Also For loops in python use generator to implement.
#! Generators save memory as they produce item one at a time thus saving lots of operations.
# ! Instead of return generators use yield keyword to produce iterable items, and instead of function name they are called using __next__() function.
# ---------------------------------------------------------------------------- #
def gen_func(a):
    yield a


a = [2, 3, 4, 5]
b = gen_func(a)  # Initializing generator and creating object named b.
print("Gen Function01:", next(b))  # Calling item of object b one at a time.
# ---------------------------------------------------------------------------- #


def new(dict):
    for x, y in dict.items():
        yield x, y


a = {1: "Hi", 2: "Welcome"}
b = new(a)
print("Generator Function02 Called for once:", next(b))
print("Generator Function02 Called twice:", next(b))
#* ------------------------------------ EOF ----------------------------------- #
