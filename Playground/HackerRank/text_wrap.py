#!/usr/bin/env python3

#! -------------------------------- Text Wrap -------------------------------- #
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

print(f"{string}\n{max_width}")
print(wrap(string, max_width))
#! ------------------------------------ EOF ----------------------------------- #
