import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    ## check if player has won
    if player.ycor() > player.FINISH_LINE_Y:
        player.resetpos()
        car_manager.faster()
        score_board.score_up()

    ## detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

score_board.game_over()
screen.exitonclick()