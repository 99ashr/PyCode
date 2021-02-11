#!/usr/bin/env python3


#! ------------------------------- string_number ------------------------------- #

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)


# print(fact(5))


def strong(n):
    s_num = str(n)
    sum = 0
    for i in s_num:
        sum += fact(int(i))
    if sum == n:
        return (f"{n} is a strong number")
    else:
        return (f"{n} is not a strong number, it's sum is {sum}")


print(strong(145))
print(strong(121))
print(strong(135))

#! ------------------------------------ EOF ----------------------------------- #
