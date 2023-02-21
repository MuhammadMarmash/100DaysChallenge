from turtle import Turtle, Screen

sami = Turtle()
screen = Screen()


def move_forward():
    sami.fd(10)


def move_backward():
    sami.bk(10)


def turn_left():
    sami.lt(10)


def turn_right():
    sami.rt(10)


def clear_all():
    screen.resetscreen()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_all, key="c")

screen.exitonclick()
