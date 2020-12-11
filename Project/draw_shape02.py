#!/usr/bin/Python3

import turtle

# set color and speed

any=turtle.Turtle()
any.color("cyan")
any.speed(0)

# function to draw shape

def draw_square():
	for side in range(4):
		any.forward(100)
		any.right(90)
		for side in range(4):
			any.forward(50)
			any.right(90)

draw_square()

def new_fun():
	for sq in range(30):
		draw_square()
		any.penup()
		any.forward(20)
		any.left(45)
		any.pendown()
new_fun()