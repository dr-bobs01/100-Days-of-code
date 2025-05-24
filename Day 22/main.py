from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

padr = Paddle((350, 0))
padl = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(padr.up,"Up")
screen.onkey(padr.down,"Down")
screen.onkey(padl.up,"w")
screen.onkey(padl.down,"s")

game_on = True
while game_on:
    time.sleep(0.0000000000000000000000000000000001)
    screen.update()
    ball.move()
    ## check & make ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ## detect collision with paddles
    if ball.distance(padr) < 50 and ball.xcor() > 330 or ball.distance(padl) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.step += 0.5

    ## detect wall hit right
    if ball.xcor() > 400:
        ball.out()
        score.r_point()
    ## detect wall hit left
    if ball.xcor() < -400:
        ball.out()
        score.l_point()
    # print(f"x:{ball.xmove} y:{ball.ymove} step:{ball.step}")

screen.exitonclick()