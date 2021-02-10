#!/usr/bin/env python3


#! ------------------------------- Greatest ------------------------------- #
# Start your code from here!
def Greatest(num):
    num.sort()
    print(f"{num[(len(num))-1]} is the Greatest of all the given numbers")


num = [99, 23, 45, 87, 56, 999, 456, 245, 647, 253, 76, 354, 765]

Greatest(num)


#! ------------------------------------ EOF ----------------------------------- #
