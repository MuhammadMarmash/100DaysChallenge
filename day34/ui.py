from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.title("Quizzler")

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text=f"score:", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1, pady=20, padx=20)

        right_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=lambda: self.answer_check(True))
        self.right_button.grid(row=2, column=1, pady=20, padx=20)
        self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.answer_check(False))
        self.false_button.grid(row=2, column=0, pady=20, padx=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_check(self, answer: bool):
        is_right = self.quiz.check_answer(f"{answer}")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
