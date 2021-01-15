#!/usr/bin/env python3

#* -------------------------------- Inheritance ------------------------------- #
class polygon():
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for _ in range(no_of_sides)]

    def input_side(self):
        self.sides = [float(input("Enter the side "+str(i+1)+" : "))
                      for i in range(self.n)]

    def display_sides(self):
        print("#--------Sides--------#")
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


# #p = polygon(3)
# #p.input_side()
# #p.display_sides()

class Triangle(polygon):
    def __init__(self):
        # polygon.__init__(self, 3)
        super().__init__(3)

    def Area(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The Area of Triangle is %0.2f Units sq" % area)


# ---------------------------------------------------------------------------- #
t = Triangle()
t.input_side()
t.display_sides()
t.Area()
#* ------------------------------------ EOF ----------------------------------- #
