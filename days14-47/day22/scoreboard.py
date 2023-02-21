from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.score}", align="center", font=("Courier", 40, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))

