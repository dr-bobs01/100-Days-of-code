import turtle
from turtle import Turtle,Screen
from random import randint

t = Turtle()
t.speed(0)
turtle.colormode(255)

for i in range(72):
    t.pencolor((randint(0, 225), randint(0, 225), randint(0, 225)))
    t.circle(100)
    t.right(5)

screen = Screen()
screen.exitonclick()
