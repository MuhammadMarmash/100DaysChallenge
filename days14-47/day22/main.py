import time
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
line = Turtle()
line.color("white")
line.hideturtle()
line.speed("fastest")
line.penup()
line.goto(x=0, y=-280)
line.lt(90)
is_on = True
while is_on:
    if line.ycor() >= 300.00:
        is_on = False
    else:
        line.pendown()
        line.fd(10)
        line.penup()
        line.fd(10)

right_player = ScoreBoard(30)
left_player = ScoreBoard(-30)

right_paddle = Paddle(screen, 360)
right_paddle.listeners("Up", "Down")
left_paddle = Paddle(screen, -360)
left_paddle.listeners("w", "s")
ball = Ball()
game_on = True
while game_on:
    ball.goto(0, 0)
    ball.move_speed = 0.1
    is_on = True
    while is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if (right_paddle.distance(ball) < 50 and ball.xcor() > 340) or (left_paddle.distance(ball) < 50 and ball.xcor() < -340):
            ball.bounce_x()
        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.bounce_y()

        if ball.xcor() >= 390:
            left_player.increase_score()
            is_on = False
        elif ball.xcor() <= -390:
            right_player.increase_score()
            is_on = False

screen.exitonclick()
