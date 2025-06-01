from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-280,y=250)
        self.score = 1
        self.hideturtle()
        self.display()

    def score_up(self):
        self.score += 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}",False, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=("Courier", 48, "bold"))
