#!/usr/bin/python3

def generate_next_date(day,month,year):

    """A Python program to display the next day date of the given one"""
    #Assignment of months
    longer_month=[1,3,5,7,8,10,12]
    shorter_month=[4,6,9,11]

    #last possible date of the month
    last_date=0

    # print(longer_month,shorter_month)
    if(month in longer_month):
    	last_date=31
    elif(month==2):
    	last_date==28
    else:
    	last_date=30
    	

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30,6,2015)