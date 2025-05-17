from scoreboard import Score
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")

score = Score()

while True:
    score.display()
    score.score += 1
    time.sleep(0.01)


screen.exitonclick()