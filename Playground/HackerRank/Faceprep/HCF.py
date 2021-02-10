#!/usr/bin/env python3


#! ------------------------------- HCF ------------------------------- #
# Start your code from here!
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


r = gcd(10, 15)
print(r)
r = gcd(18, 12)
print(r)
r = gcd(18, gcd(27, 24))
print(r)

#! ------------------------------------ EOF ----------------------------------- #
