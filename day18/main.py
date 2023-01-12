import turtle
from random import choice, randint

turtle.colormode(255)
sami = turtle.Turtle()
sami.shape("turtle")
sami.speed("fastest")
# sami.width(15)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
          "SlateGray", "SeaGreen"]

# square
# for i in range(4):
#     sami.right(90)
#     sami.forward(150)

# dashed line
# for i in range(15):
#     sami.down()
#     sami.fd(10)
#     sami.up()
#     sami.fd(10)

# random shapes
# for sides in range(3, 11):
#     sami.color(random.choice(colors))
#     for _ in range(sides):
#         sami.rt(360 / sides)
#         sami.fd(100)

# random walk
# angels = [0, 90, 180, 270]
#
# for _ in range(200):
#     sami.color(choice(colors))
#     # hard
#     # choice([sami.rt(choice(angels)), sami.lt(choice(angels))])
#     # easy
#     sami.setheading(choice(angels))
#     sami.fd(30)
# Spirograph
# circles = 50
# for _ in range(circles):
#     sami.color((randint(0, 255), randint(0, 255), randint(0, 255)))
#     sami.circle(100)
#     sami.lt(360/circles)


screen = turtle.Screen()
screen.exitonclick()
