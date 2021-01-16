#!/usr/bin/env python3

#* --------------------------- Demonstration of MRO --------------------------- #
# @MRO --> Method Resolution Order
# ! MRO is used to find the order of the class when the principal of Inheritance is used. MRO of a class can be viewed as the __mro__ attribute or the mro() method. The former returns a tuple while the latter returns a list.

# ---------------------------------------------------------------------------- #

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass

# ---------------------------------- Output ---------------------------------- #
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]


# print(M.mro())
order = M.mro()
for i in order:
    print(i)

#* ------------------------------------ EOF ----------------------------------- #
