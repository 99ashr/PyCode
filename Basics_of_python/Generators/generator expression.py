#!/usr/bin/env python3

#* --------------------------- Generator Expression --------------------------- #
# ! Just like lambda function and list comprehension generator expressions are used to create anonymous generator function.
# ---------------------------------------------------------------------------- #

#* ---------------------------- list comprehension ---------------------------- #
# r = [u+2 for u in range(6, 0, -1)]
# print("r:", r)

a = range(6, 0, -1)
print("Generator expression", end=":\t")
c = (x+2 for x in a)
print(c)  # This is gonna give the generator function id as output
# print(min(c))  # Minimum of all the numbers
# To get the result out of a generator expression use a for loop
print("Generator Expression Output: ")
for r in c:
    print(r)
#* ------------------------------------ EOF ----------------------------------- #
