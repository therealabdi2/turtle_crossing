from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.mov_speed = STARTING_MOVE_DISTANCE

    def mov_car(self):
        for car in self.all_cars:
            car.forward(self.mov_speed)

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def inc_speed(self):
        self.mov_speed += MOVE_INCREMENT
