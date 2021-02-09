#!/usr/bin/env python3


#! ------------------------------- Prime_Number ------------------------------- #
# Start your code from here!
def prime(n):
    for i in range(3, n):
        if n % i == 0:
            return (f"{n} is not a prime number")
    return (f"{n} is a prime number")


print(prime(13))
print(prime(15))
print(prime(17))
print(prime(21))
print(prime(26))
#! ------------------------------------ EOF ----------------------------------- #
