from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[-1].penup()
    turtles[-1].color(color)
    turtles[-1].goto(x=-290, y=290-(80*(len(turtles)-1)))

is_race_on = True
winner = ""
while is_race_on:
    for turn in turtles:
        turn.fd(randint(a=0, b=10))
        if turn.position()[0] >= 270:
            is_race_on = False
            winner = turn.color()[0]
            break

if user_bet.lower() == winner:
    print(f"You've won! The{winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")
screen.exitonclick()
