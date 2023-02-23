from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(x=-220, y=260)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over", align="center", font=FONT)
