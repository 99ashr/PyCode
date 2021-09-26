#!/usr/bin/env python3

#! ----------------------------- String Capitalize ---------------------------- #

# ---------------------------------------------------------------------------- #

#** ---------------------------------- Inputs ---------------------------------- #

s = 'chris alan'
s1 = '12abc'
s2 = 'ram prasad sharma'
s3 = "1 2 2 3 4 5 6 7 8  9"
s4 = 'ram12 praSAd 12shArma   ansari khan_thakur '

# ---------------------------------------------------------------------------- #


def solve(s):
    l = []
    s = s.split(" ")
    for i in s:
        l.append(i.capitalize())
    k = " ".join(l)
    return k


print(solve(s))
print(solve(s1))
print(solve(s2))
print(solve(s3))
print(solve(s4))

#! ------------------------------------ EOF ----------------------------------- #
