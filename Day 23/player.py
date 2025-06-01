from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.penup()
        self.resetpos()
        self.left(90)
        self.FINISH_LINE_Y = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def resetpos(self):
        self.goto(STARTING_POSITION)
