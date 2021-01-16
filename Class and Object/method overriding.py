#!/usr/bin/env python3

#* ----------------------------- Method Overriding ---------------------------- #
#! Things like these occur while inheriting classes who have same method names. In that case the preference is given to the current class instead of parent class.

# ---------------------------------------------------------------------------- #
class parent():
    def func(self):
        print("This is the Parent class function!!!")


class child(parent):
    def func(self):
        print("This is the child class function!!!")
# ---------------------------------------------------------------------------- #


obj = child()
obj.func()
#! This functionality comes in handy whenever we want to change the application of the parent method.
#* ------------------------------------ EOF ----------------------------------- #
