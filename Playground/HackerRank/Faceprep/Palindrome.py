#!/usr/bin/env python3

#! ---------------------- Palindrome (Number and String) ---------------------- #
n = 12321
s = 'malayalam'


def palindrome(var):
    if type(var) == int:
        var = str(var)
        if var == var[::-1]:
            print(f"{var} is a Palindrome number")
        else:
            print(f"{var} is not a Palindrome number")
    elif type(var) == str:
        if var == var[::-1]:
            print(f"{var} is a Palindrome number")
        else:
            print(f"{var} is not a Palindrome number")
    else:
        print(".......")


palindrome(n)
#! ------------------------------------ EOF ----------------------------------- #
