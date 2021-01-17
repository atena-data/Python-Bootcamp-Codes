from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=500, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(250,
                                                125,
                                                text="",
                                                width=280,
                                                fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # set score label
        self.label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)
        self.label.config(padx=20, pady=20)

        # set buttons
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image,
                                  bg=THEME_COLOR,
                                  highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image,
                                   bg=THEME_COLOR,
                                   highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz...")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

