#!/bin/python3

import math


class Rectangle:
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth*self.length


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)


if __name__ == '__main__':
