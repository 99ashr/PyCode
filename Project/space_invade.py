import turtle
from turtle import forward, right, left
forward(50)
import os
import math
import random
import shelve

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space invaders")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
     border_pen.fd(600)
     border_pen.lt(90)
border_pen.hideturtle()

delay = input("press enter to finish.")