#!/usr/bin/python3

def form_triangle(num1,num2,num3):
    """This program checks the sides of a triangle are valid or not"""
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    if num1<(num2+num3):
        if num2<(num3+num1):
            if num3<(num1+num2):
                return success
            else:
                return failure
        else:
            return failure
    else:
        return failure
    
    

#Provide different values for the variables, num1, num2, num3 and test your program
num1=12
num2=7
num3=3
form_triangle(num1, num2, num3)