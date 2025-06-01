from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            newcar = Turtle("square")
            newcar.shapesize(stretch_wid=1,stretch_len=2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            newcar.setpos(x = 300 ,y = random.randint(-250,250))
            self.all_cars.append(newcar)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def faster(self):
        self.car_speed += MOVE_INCREMENT

