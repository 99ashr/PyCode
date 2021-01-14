#!/usr/bin/env python3

#* -------------------------------- Inheritance ------------------------------- #

#& ------------------------------- Parent Class ------------------------------- #

class parent():
    def __init__(self, class_name="Parent Class"):
        self.class_name = class_name
        print("We're in the", class_name, "Constructor")

    def display(self):
        print("We're in Parent class display")
        print(self.class_name)


# # p = parent()
# # p.display()

#& -------------------------------- Child Class ------------------------------- #


class child01(parent):
    def __init__(self, child_class_name="Child Class"):
        super().__init__()
        self.child_class_name = child_class_name
        print("We're in the", child_class_name, "Constructor")

    def display_child(self):
        print("We're in the child class display")
        print(self.child_class_name)


c1 = child01()
c1.display()
c1.display_child()

#* ------------------------------------ EOF ----------------------------------- #
