import turtle
from random import randint

turtle.colormode(255)


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.segments = []
        for _ in range(3):
            self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments.append(turtle.Turtle("square"))
        self.segments[-1].color((randint(0, 255), randint(0, 255), randint(0, 255)))

        self.segments[-1].penup()
        if len(self.segments) != 1:
            last_segment_place = self.segments[-2].position()
            self.segments[-1].goto(x=(last_segment_place[0] - 20), y=last_segment_place[1])

    def listen(self):
        def up():
            if self.head.heading() != 270:
                self.head.setheading(90)

        def down():
            if self.head.heading() != 90:
                self.head.setheading(270)

        def right():
            if self.head.heading() != 180:
                self.head.setheading(0)

        def left():
            if self.head.heading() != 0:
                self.head.setheading(180)

        self.screen.listen()
        self.screen.onkeypress(key="w", fun=up)
        self.screen.onkeypress(key="s", fun=down)
        self.screen.onkeypress(key="d", fun=right)
        self.screen.onkeypress(key="a", fun=left)

    def move(self):
        for i in range(1, len(self.segments)):
            self.segments[-i].goto(self.segments[-i - 1].position())
        self.head.fd(20)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        for _ in range(3):
            self.create_snake()
        self.head = self.segments[0]
