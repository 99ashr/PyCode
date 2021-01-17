#!/usr/bin/env python3

#* ---------------------- Decorated function for division --------------------- #
# & Syntax--> Decorators can be defined or called using '@' symbol above the definition of the method that you want to call.
# ---------------------------------------------------------------------------- #
def smart_divide(func):
    def inner_func(a, b):
        print("We're dividing", a, "and", b)
        if b == 0:
            # print("Whoops, we can't divide that")
            return "Whoops, we can't divide that"
        return func(a, b)
    return inner_func


@smart_divide
def divide(a, b):
    return(a/b)


d = divide(2, 5)
print(d)
d = divide(2, 0)
print(d)
#* ------------------------------------ EOF ----------------------------------- #
