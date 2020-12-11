#!/usr/bin/python3

"""A python program to display the product of three numbers based upon following rules: 
    if the value of one the integer is 7 then it should not be included and 
    the values along its right should also be ignored
    In case there's 7 on the unit place display -1 as the output"""

def find_product(num1,num2,num3):
    product=0

    if num1==7:
        product=num2*num3
    elif num2==7:
        product=num3
    elif num3==7:
        product=-1
    else:
        product=num1*num2*num3
        
    return product

product=find_product(7,6,2)
print(product)