import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
sami = turtle.Turtle()
sami.penup()
sami.hideturtle()
screen.tracer(0)
data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
while score != 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        score += 1
        correct_answer_data = data[data.state == answer_state]
        sami.goto(x=int(correct_answer_data.x), y=int(correct_answer_data.y))
        sami.write(correct_answer_data.state.item())
        data = data.drop([correct_answer_data.index.item()])
        print(data)

