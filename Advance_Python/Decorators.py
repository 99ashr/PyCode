#!/usr/bin/env python3

#* --------------------------------- Decorators -------------------------------- #
#! Everything in python is object and these objects can be bound to another name/variable to call them.
def first(msg):
    print(msg)


# first("Hello")

second = first
# second("Hello")
# ---------------------------------------------------------------------------- #


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


# print(operate(inc, 3))
# print(operate(dec, 3))
# ---------------------------------------------------------------------------- #

def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()
# new()
#* ------------------------------------ EOF ----------------------------------- #
