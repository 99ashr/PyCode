#! /usr/bin/python3

import unicodedata as uni

# unicodedata contains detail about all the special characters

mark=input('Enter the character: ')

m=uni.name(mark)
print(m)