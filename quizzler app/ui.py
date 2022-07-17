from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
score = 0


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="questions", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # label
        self.score_label = Label(text=f"Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # buttons
        correct_img = PhotoImage(file="quizzler app/images/true.png")
        self.correct_button = Button(
            image=correct_img, highlightthickness=0, command=self.guessed_true)
        self.correct_button.grid(row=2, column=0)
        incorrect_img = PhotoImage(file="quizzler app/images/false.png")
        self.incorrect_button = Button(
            image=incorrect_img, highlightthickness=0, command=self.guessed_false)
        self.incorrect_button.grid(row=2, column=1)
        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have finished the quiz.")
            self.incorrect_button.config(state="disabled")
            self.correct_button.config(state="disabled")

    def guessed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def guessed_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_ques)
