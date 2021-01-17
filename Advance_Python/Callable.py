#!/usr/bin/env python3

#* ------------------------ Function returning function ----------------------- #
def is_called():
    def is_returned():
        return ("Hello")
    return is_returned

# ! To return a function just use the function name without parentheses signs


is_return = is_called()
# new = is_return()
# print(new)
print(is_return())

#* ------------------------------------ EOF ----------------------------------- #
