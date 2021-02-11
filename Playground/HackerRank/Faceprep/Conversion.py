#!/usr/bin/env python3


#! ------------------------------- Conversion ------------------------------- #
# Start your code from here!
# &  Decimal-->Binary; Binary-->Hexadecimal; Binary-->Octal; Decimal--> Octal; Decimal-->Hexadecimal; Octal-->Hexadecimal
n = 19


def D2B(n):
    return int(bin(n)[2:])


def D2O(n):
    return int(oct(n)[2:])


def D2H(n):
    return int(hex(n)[2:])


def B2D(b):
    num = int(str(b), 2)
    return int(num)

# ------------------------------------ OR ------------------------------------ #


def B2D_extended(b):
    l = len(b) - 1
    num = 0
    for i in b:
        num += int(i) * 2 ** l
        l -= 1
    return num


def B2O(b):
    return int(oct(int(b))[2:])


def B2H(b):
    return hex(int(b))[2:]


def O2D(o):
    num = int(str(o), 8)
    return num


def H2D(h):
    num = int(str(h), 16)
    return num


print(f"Binary-->Decimal: {B2D(D2B(n))}")
# print(f"Binary-->Octal: {B2O(D2B(n))}")
# print(f"Binary to Hexadecimal: {B2H(D2B(n))}")


print(f"Decimal-->Binary: {D2B(n)}")
print(f"Decimal-->Octal: {D2O(n)}")
print(f"Decimal-->Hexadecimal: {D2H(n)}")

print(f"Octal-->Decimal: {O2D(23)}")

print(f"Hexadecimal-->Decimal: {H2D(13)}")
#! ------------------------------------ EOF ----------------------------------- #
