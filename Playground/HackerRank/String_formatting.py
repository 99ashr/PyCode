#!/usr/bin/env python3

#! --------------------- String Formatting and Conversion --------------------- #
n = 63
blen = (bin(n)[2:])
w = len(blen)
# print(w)
for i in range(1, n+1):
    print(
        f"{str(i).rjust(w)} {oct(i)[2:].rjust(w)} {hex(i)[2:].upper().rjust(w)} {bin(i)[2:].rjust(w)}")
#! ------------------------------------ EOF ----------------------------------- #
