from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor("black")
wn.title("Space invaders")

border_pen = Turtle()
border_pen.speed("fastest")
border_pen.color("white")
border_pen.pensize(3)

border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

border_pen.hideturtle()

wn.exitonclick()