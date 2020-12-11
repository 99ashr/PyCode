#!/usr/bin/Python3

# importing turtle for drawing shapes

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

# Do not draw

any.penup()
any.back(20)

any.pendown()

for square in range(75):
	draw_square()
	any.forward(5)
	any.left(5)

any.hideturtle()