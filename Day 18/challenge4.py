import turtle
from turtle import Turtle,Screen
from random import randint

t = Turtle()
t.width(50)
t.speed(0)
turtle.colormode(255)

def right():
    t.forward(100)
def left():
    t.right(180)
    t.forward(100)
    t.right(180)
def up():
    t.left(90)
    t.forward(100)
    t.right(90)
def down():
    t.right(90)
    t.forward(100)
    t.left(90)

while True:
    t.pencolor((randint(0, 225), randint(0, 225), randint(0, 225)))
    num = randint(1,4)
    if num == 1:
        right()
    elif num == 2:
        left()
    elif num == 3:
        up()
    elif num == 4:
        down()

screen = Screen()
screen.exitonclick()