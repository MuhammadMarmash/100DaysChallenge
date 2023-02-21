from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_amount = 10
        self.y = choice([-self.move_amount, self.move_amount])
        self.x = choice([-self.move_amount, self.move_amount])
        self.move_speed = 0.1

    def move(self):
        self.goto(x=(self.xcor() + self.x), y=(self.ycor() + self.y))

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

