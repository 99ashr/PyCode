# def sq(a): return a*a
# print(sq(3))

# @ Filter function
# & Syntax --> filter(function,iterable)

# ----------------------------------- Algo ----------------------------------- #
# ! required--> List of marks :mylist
# ! i) Generate another list using list keyword
# ! ii) filter every number from mylist and using the lambda function match the expression
# ! Display the output
# ---------------------------------------------------------------------------- #

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = list(filter(lambda x: x % 3 == 2, mylist))
# print(new_list)


# @ Map function
# & Syntax --> map(function,iterable)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x: x % 3 == 2, mylist))
print(new_list)
