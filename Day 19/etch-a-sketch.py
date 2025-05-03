from turtle import  Turtle, Screen

t = Turtle()
screen = Screen()

## set how much you move
turn = 20
step = 20

def move():
    t.forward(step)
def back():
    t.back(step)
def left():
    t.left(turn)
def right():
    t.right(turn)
def clear():
    t.home()
    t.clear()

screen.listen()
screen.onkey(key="w",fun=move)
screen.onkey(key="a",fun=left)
screen.onkey(key="s",fun=back)
screen.onkey(key="d",fun=right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
