#!/usr/bin/pyhton3

import turtle

def spiral(side,turn,color,width):
	t=turtle.Turtle()
	t.color(color)
	t.speed(0)
	t.width(width)
	for n in range(side):
		t.forward(n)
		t.right(turn)
spiral(150,45,'cyan',5)