#!/usr/bin/env python3

#* ----------------------------- Fibonacci Series ----------------------------- #
# ! A series of numbers where each number is a sum of previous two numbers.
# & Syntax -->a=0,b=1,c=1,d=2 i.e (a=b and b=a+b)
def fibonacci():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f+s


for i in fibonacci():
    if i > 50:
        break
    print(i, end=" ")
#* ------------------------------------ EOF ----------------------------------- #
