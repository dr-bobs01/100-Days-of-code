from turtle import  Turtle, Screen

t = Turtle()
screen = Screen()

def move():
    t.forward(10)

screen.listen()
screen.onkey(key="space",fun=move)

screen.exitonclick()
