from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz:QuizBrain):
        self.question = quiz
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(pady=50, padx=50, bg=THEME_COLOR, highlightthickness=0)
        self.score_label = Label(text="Score: 0", font=("Arial", 20, "bold"), highlightthickness=0, background=THEME_COLOR)
        self.canvas = Canvas(width=350, height=250)
        self.quiz_text = self.canvas.create_text(175, 125, text="Hello", font=("Arial", 20, "italic"), width=300)
        self.tick_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick_image, highlightthickness=0, bg=THEME_COLOR, command=self.tick_check)
        self.cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, bg=THEME_COLOR, command=self.cross_check)

        # Layout
        self.score_label.grid(column=1, row=0, pady=20)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.tick_button.grid(column=1, row=2, pady=30)
        self.cross_button.grid(column=0, row=2, pady=30)
        self.display_question()
        self.window.mainloop()

    def display_question(self):
        self.canvas.config(bg="white")
        if self.question.still_has_questions():
            question_text = self.question.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You are out of questions.")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def tick_check(self):
        is_right = self.question.check_answer("True")
        self.give_feedback(is_right)

    def cross_check(self):
        is_right = self.question.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, condition):
        if condition:
            self.canvas.configure(background="green")
            self.update_score()
        else:
            self.canvas.configure(background="red")
        self.window.after(1000, self.display_question)

    def update_score(self):
        current_score = self.question.score
        self.score_label.config(text=f"Score: {current_score}")
