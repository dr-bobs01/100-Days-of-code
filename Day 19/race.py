from turtle import  Turtle, Screen
from random import randint

race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make a bet", "Which turtle will win the race? Enter a color: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
startpos = 0

for i in colours:
    col = i
    i = Turtle(shape="turtle")
    i.penup()
    i.color(col)
    i.goto(-230,startpos-50)
    startpos += 30
    turtles.append(i)

if user_bet:
    race_on = True

while race_on:
    for i in turtles:
        if i.xcor() > 230:
            race_on = False
            winner = i.pencolor()
            if winner == user_bet:
                print(f"You won! {winner} won!")
            else:
                print(f"You lost. {winner} won.")
        i.forward(randint(0,10))

screen.exitonclick()
