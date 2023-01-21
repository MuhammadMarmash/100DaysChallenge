from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = []
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/english_words.csv")

to_learn = data.to_dict(orient="records")


screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flashy")
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Are You Ready???", font=("Ariel", 60, "bold"), justify="right")
canvas.grid(row=0, column=0, columnspan=2)

current_card = {}


def next_card(known):
    global current_card, timer, words_to_learn
    screen.after_cancel(timer)
    if known:
        to_learn.remove(current_card)
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("data/words_to_learn.csv", index=False)
    current_card = choice(to_learn)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer = screen.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_text, text="Arabic", fill="white")
    canvas.itemconfig(word_text, text=str(current_card["Arabic"])[::-1], fill="white")


timer = screen.after(3000, func=lambda: next_card(False))
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda: next_card(False))
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=lambda: next_card(True))
right_button.grid(row=1, column=1)

screen.mainloop()
