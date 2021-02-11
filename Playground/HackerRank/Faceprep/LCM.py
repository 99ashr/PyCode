#!/usr/bin/env python3
#! ------------------------------- LCM ------------------------------- #


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    p = a * b
    lcm = int(p / gcd(a, b))
    return lcm


print(f"LCM: {lcm(9, 12)}")

#! ------------------------------------ EOF ----------------------------------- #
