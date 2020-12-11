#!/usr/bin/python3

def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    y=given_year
    if y%4==0:
        if y%100==0:
            if y%400==0:
                print('leap year')
            else:
                print('non leap')
        else:
            print('leap year')
    else:
        print('non leap')

    return list_of_leap_years

list_of_leap_years=find_leap_years(2004)
print(list_of_leap_years)