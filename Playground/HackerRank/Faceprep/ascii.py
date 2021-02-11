#!/usr/bin/env python3


#! ------------------------------- ascii ------------------------------- #
# Start your code from here!
def ascii(val):
    if type(val) == int:
        return chr(val)
    elif type(val) == str:
        return ord(val)
    else:
        return "Enter Correct Value"


print(ascii(97))
print(ascii("Z"))
print(ascii(986))
print(ascii(197))
print(ascii('z'))
print(ascii('g'))

#! ------------------------------------ EOF ----------------------------------- #
