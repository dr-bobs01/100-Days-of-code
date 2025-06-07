from turtle import Turtle
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.segments  = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for num in range(3):
            x = 0
            self.add_segment((x,0))
            x -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x,y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self,position):
        num = Turtle(shape="square")
        num.color("white")
        num.penup()
        num.setpos(position)
        self.segments.append(num)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
