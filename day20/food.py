import turtle
from random import choice, randint

turtle.colormode(255)


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.position_range = range(-280, 280, 20)
        self.refresh()

    def refresh(self):
        self.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        self.goto(choice(self.position_range), choice(self.position_range))
