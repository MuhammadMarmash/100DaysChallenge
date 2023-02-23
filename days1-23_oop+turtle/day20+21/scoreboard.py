from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score: {self.score} High Score: {self.high_score}",
                   align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    # def game_over(self):
    #     self.reset()
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align="center", font=("Courier", 24, "normal"))

