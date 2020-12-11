#!/usr/bin/Python3

import turtle

# set color and speed

any=turtle.Turtle()
any.color("cyan")
any.speed(0)
colors=['green','firebrick','orange','navy','lightblue','purple','violet','yellow']
# function to draw shape

def draw_square(colors):
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

for color in colors:
	any.color(color)
	draw_square(colors)
	any.forward(50)
	any.left(45)

# any.hideturtle()