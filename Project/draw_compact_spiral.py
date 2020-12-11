#!/usr/bin/python3

from turtle import Turtle,Screen

wn=Screen()
wn.bgcolor('black')
wn.title('Pizza')
# wn.bgpic('smoking_girl.jpeg')

def spiral(sides,turn,color,width):
	t=Turtle()
	# t.screen.bgpic('./smoking_girl.jpeg')
	t.color(color)
	t.shape('turtle')
	t.speed(0)
	t.width(width)
	for n in range(sides):
		t.forward(n)
		t.right(turn)
		t.penup()
		t.left(60)
		t.forward(10)
		t.right(60)
		t.pendown()
		t.hideturtle()
spiral(130,60,'cyan',.5)

wn.exitonclick()