#!/usr/bin/env python3


#! ------------------------------- power_recusrion ------------------------------- #

# ---------------------------------------------------------------------------- #
#                             Power using Recursion                            #
# ---------------------------------------------------------------------------- #

# ---------------------------- for integer inputs ---------------------------- #

def power(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return(n*power(n, m-1))


inp = int(input(
    "Choose your prefered input type: \n 1. Press 1 for INTEGER \n 2. Press 2 for STRING \n\t\t"))

if inp == 1:
    n = int(input("Enter the number: "))
    m = int(input("Enter the power: "))

    print(str(n)+"^"+str(m)+" = "+str(power(n, m)))

elif inp == 2:
    n = str(input("Enter the number: "))
    m = str(input("Enter the power: "))

    print(n+"^"+m+" = "+str(power(int(n), int(m))))


# print(power(n, m)) str(power(n, m))
# print(str(n)+"^"+str(m)+" = "+str(power(n, m)))


# ---------------------------- with string inputs ---------------------------- #


# print(n+"^"+m+" = "+str(power(int(n), int(m))))


#! ------------------------------------ EOF ----------------------------------- #
