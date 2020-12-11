#!/usr/bin/python3

def temperature(celsius=0,fahrenheit=0):
	"""This python program returns """
    if celsius==0:
        # find celsius
        celsius=(fahrenheit-32)*(5/9)
        return celsius
    elif fahrenheit==0:
        fahrenheit=celsius*(9/5)+32
        return fahrenheit
    else:
        print("please pass a valid input")
        
temp=temperature(fahrenheit=98)
print(temp)