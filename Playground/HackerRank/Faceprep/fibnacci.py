#!/usr/bin/env python3


#! ------------------------------- fibnacci ------------------------------- #
#Start your code from here!
def fib(n):
    a,b=1,2
    print(a)
    for _ in range(1,n):
        print(b)
        c=b+a
        a,b=b,c

fib(10)

#! ------------------------------------ EOF ----------------------------------- #