from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coord):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.goto(coord)

    def up(self):
        self.sety(self.ycor()+20)
    def down(self):
        self.sety(self.ycor()-20)
