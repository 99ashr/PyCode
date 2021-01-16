#!/usr/bin/env python3

#* ------------------------------- Introdunction ------------------------------ #
# ! Entire program is defined as class and object. Everything that is similar is termed as class and every method,variable etc is an object.
# ! A class is a logical grouping which can be reused. Can also be termed as Template.
# & Syntax --> Class <class_name>:
# ---------------------------------------------------------------------------- #

#* ----------------------------------- Class ---------------------------------- #

class Car():
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def price_inc(self):
        self.price = int(self.price*1.15)


#* ---------------------------------- Object ---------------------------------- #
honda = Car("City", 2016, 10000789)

#* ------------------------------ Display object ------------------------------ #
print(honda.__dict__)  # Everything that an object holds
honda.cc = 1500  # New data to honda object
print(honda.cc)  # display a particular object detail
print(honda.__dict__)

# ---------------------------------- Output ---------------------------------- #

{'model': 'City', 'year': 2016, 'price': 10000789}
1500
{'model': 'City', 'year': 2016, 'price': 10000789, 'cc': 1500}

# ---------------------------------------------------------------------------- #
#* ------------------------------------ EOF ----------------------------------- #
