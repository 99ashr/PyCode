#!/usr/bin/Python3

from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor("black")
wn.title("I Love You")
j=Turtle()
r=Turtle()
j.color('misty rose')
j.width(3)
r.color('firebrick')
r.width(3)
r_lst_name='Montague'
r.left(40)
r.forward(100)
for side in range(185):
	r.forward(1)
	r.left(1)
r.hideturtle()

if r_lst_name=='Montague':
	j.left(140)
	j.forward(100)
	for side in range(185):
		j.right(1)
		j.forward(1)

wn.exitonclick()