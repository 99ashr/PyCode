#!/usr/bin/env python3

#! ----------------------------- string validation ---------------------------- #

s = "qA2"
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))
#! ------------------------------------ EOF ----------------------------------- #
