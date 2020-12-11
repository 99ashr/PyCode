#!/usr/bin/Python3

# importing calender to display calendar
import calendar

#date module can give current date and time
import datetime as d

date=str(d.datetime.now().date())


# year=str(date[0:4])

year=2019
month=8

# month=str(date[5:7])

cal=calendar.month(2019,8)
print(cal)