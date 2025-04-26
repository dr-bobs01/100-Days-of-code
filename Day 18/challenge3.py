from turtle import Turtle,Screen,colormode
from random import randint
sides = 3
colormode(255)
t = Turtle()
for i in range(6):
    num1 = randint(0, 225)
    num2 = randint(0, 225)
    num3 = randint(0, 225)

    t.pencolor((num1, num2, num3))
    angle = 360 / sides
    for x in range(sides):
        t.rt(angle)
        t.forward(100)
    sides += 1

screen = Screen()
screen.exitonclick()