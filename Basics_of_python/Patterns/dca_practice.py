#!/usr/bin/env python3

# ---------------------------------------------------------------------------- #
#                       dca_practice                      #
# ---------------------------------------------------------------------------- #


#! -------------------------------   # SubHeading!------------------------------- #
# Start your code from here!
# -------------------- Multiply Digits of a string number -------------------- #

# string_=input("Enter the string Number here: ")
str_num = "2345"


def mul_string(string_num):
    n = 1
    for i in string_num:
        n = n*int(i)
        # print(i, n)
    return n


# print(mul_string(str_num))

# ------------------------ Remove 7 & 56 from a string ----------------------- #
str1 = "queue7cod56er"
str2 = "tcs7dca7rock57"


def remove_num(s):
    s = s.replace('7', '').replace('56', '')
    print(s)


# remove_num(str1)
# remove_num(str2)

# -------------------------------- Subsequence ------------------------------- #

subsequence = [2, 202, 3, 200, 4, 5]


def profit(l):
    m = []
    for i in range(len(l)):
        if l[i] < l[i+1]:
            m.append(l[i])
        if l[i] > l[i+1]:
            break
    print(m)


profit(subsequence)


#! ------------------------------------ EOF ----------------------------------- #
