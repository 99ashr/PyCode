from functools import reduce
def sq(a): return a*a


print(sq(3))

# @ Filter function
# & Syntax --> filter(function,iterable)

# ----------------------------------- Algo ----------------------------------- #
# ! required--> List of marks :mylist
# ! i) Generate another list using list keyword
# ! ii) filter every number from mylist and using the lambda function match the expression
# ! Display the output
# ---------------------------------------------------------------------------- #

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(filter(lambda x: x % 3 == 2, mylist))
print(new_list)


# @ Map function
# & Syntax --> map(function,iterable)

# ----------------------------------- Algo ----------------------------------- #
# ! Generate a list
# ! create a new list which maps every value in the previous list and checks weather the expression is true or false
# ---------------------------------------------------------------------------- #

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x: x % 3 == 2, mylist))
print(new_list)


# @ Reduce function from functools
# & Syntax --> reduce(function,sequence)

# ----------------------------------- Algo ----------------------------------- #
# ! reduce is a function of functools library, which undergoes the process of expression in a sequence i.e fifo...
# ---------------------------------------------------------------------------- #

p = reduce(lambda a, b: a+b, [23, 56, 43, 98, 1])
print(p)

# ------------------------------ Linear Equation ----------------------------- #


def sq2(a): return a*a


print(sq2(4))

# 3x+4y


def ex(x, y): return 3*x+4*y


print(ex(4, 7))

# ---------------------------- quadratic equation ---------------------------- #
# (a+b)^2


def quard(a, b): return (a+b)**2


print(quard(2, 3))

#* ------------------------------------ EOF ----------------------------------- #
