#!/usr/bin/python3

from turtle import Turtle,Screen
wn=Screen()
wn.bgcolor('black')
wn.title('Rangoli')
t=Turtle()
t.color('cyan')
t.speed(0)

def draw_rangoli(length):
	for side in range(4):
		t.forward(length)
		t.right(90)
		for side in range(4):
			t.forward(50)
			t.right(90)
t.penup()
t.back(20)
t.pendown()
for sq in range(80):
	draw_rangoli(5)
	t.forward(5)
	t.left(5)
t.hideturtle()

wn.exitonclick()