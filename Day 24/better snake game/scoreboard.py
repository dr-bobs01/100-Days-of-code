from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.speed("fastest")
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0,265)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=("Arial", 20, 'normal'))

    def ate(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

