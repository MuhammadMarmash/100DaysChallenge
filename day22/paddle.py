from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen, x):
        super().__init__()
        self.screen = screen
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x, y=0)

    def listeners(self, up, down):
        def move_up():
            self.goto(x=self.xcor(), y=(self.ycor() + 20))

        def move_down():
            self.goto(x=self.xcor(), y=(self.ycor() - 20))

        self.screen.onkeypress(key=up, fun=move_up)
        self.screen.onkeypress(key=down, fun=move_down)
