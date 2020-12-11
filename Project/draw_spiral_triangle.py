#!/usr/bin/Python3

from turtle import Turtle,Screen

wn = Screen()
wn.bgcolor("black")
wn.title("Space invaders")


t=Turtle()
t.color('cyan')
for side in range(19):
	t.forward(10*side)
	t.right(360/3)
	t.hideturtle()

wn.exitonclick()