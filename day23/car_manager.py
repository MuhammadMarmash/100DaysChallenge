import random
from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self,):
        self.level = 1
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, (6-self.level))
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self, car):
        car.bk(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (self.level - 1)))
