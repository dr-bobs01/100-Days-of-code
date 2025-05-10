from turtle import Screen,Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = (Snake())
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")

game_on = True
while game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)


screen.exitonclick()
