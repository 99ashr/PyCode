#!/usr/bin/env python3


#! ------------------------------- Factorial ------------------------------- #
# Start your code from here!
def factorial(n):
    if n < 2:
        return n
    else:
        return n*factorial(n-1)


print(factorial(5))
print(factorial(7))
print(factorial(9))
#! ------------------------------------ EOF ----------------------------------- #
