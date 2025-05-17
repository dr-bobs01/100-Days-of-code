from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0,265)

    def ate(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 20, 'normal'))