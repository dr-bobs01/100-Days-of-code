from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.step = 1
        self.xmove = 1
        self.ymove = 1

    def move(self):
        self.sety(self.ycor() + (self.ymove * self.step))
        self.setx(self.xcor() + (self.xmove * self.step))

    def bounce_x(self):
        self.xmove *= -1

    def bounce_y(self):
         self.ymove *= -1

    def out(self):
        self.bounce_x()
        self.home()
        self.step = 1
