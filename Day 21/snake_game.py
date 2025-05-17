from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.extend,"f")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    ## detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.ate()
        snake.extend()
    ## detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    ## detect tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            game_on = False
            score.game_over()

screen.exitonclick()
