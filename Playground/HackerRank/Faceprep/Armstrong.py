#!/usr/bin/env python3


#! ------------------------------- Armstrong ------------------------------- #
# Start your code from here!
def armstrong(n):
    s = str(n)
    l = len(s)
    sum = 0
    for i in s:
        sum += int(i)**l
    if sum == n:
        return (f"{n} is an Armstrong number")
    else:
        return (f"{n} is not an Armstrong number, sum of their digits is {sum}")


print(armstrong(153))
print(armstrong(121))
print(armstrong(254))
#! ------------------------------------ EOF ----------------------------------- #
