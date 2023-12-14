from tkinter import *
from quiz_brain import  QuizBrain


THEME_COLOR = "#375362"
score = 0

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz_Brain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas= Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text = "Question here",
            fill= THEME_COLOR,
            font=("Ariel", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2,padx=20 , pady=20)

        self.score_title = Label(text=f"Score:{score}", font=("Ariel", 16, "italic"), bg=THEME_COLOR, fg="white") # Positions relative to canvas
        self.score_title.grid(row=0,column=1,padx=20 , pady=20)


# BUTTONS #

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command= self.false_pressed)
        self.false_button.grid(column=1, row=2,padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_title.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz completed !")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedack(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedack(is_wrong)

    def give_feedack(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)