#!/usr/bin/env python3


#! ------------------------------- Leap_year ------------------------------- #
# Start your code from here!
# year = '1996'


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year***")
            else:
                print(f"{year} is not a leap year***")

        else:
            print(f"{year} is a leap year*")
    else:
        print(f"{year} is not a leap year*")


leap_year(1996)
leap_year(2000)
leap_year(3000)
leap_year(4000)
leap_year(2012)
leap_year(2019)
leap_year(2020)
#! ------------------------------------ EOF ----------------------------------- #
