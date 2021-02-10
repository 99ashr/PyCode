#!/usr/bin/env python3


#! ------------------------------- Conversion ------------------------------- #
# Start your code from here!
# &  Decimal-->Binary; Binary-->Hexadecimal; Binary-->Octal; Decimal--> Octal; Decimal-->Hexadecimal; Octal-->Hexadecimal
n = 19


def D2B(n):
    return bin(n)[2:]


def D2O(n):
    return oct(n)[2:]


def D2H(n):
    return hex(n)[2:]


def B2D(x):
    return


print(f"Decimal-->Binary: {D2B(n)}")
print(f"Decimal-->Octal: {D2O(n)}")
print(f"Decimal-->Hexadecimal: {D2H(n)}")


#! ------------------------------------ EOF ----------------------------------- #
