THEME_COLOR = "#375362"
from tkinter import *


class QuizInterface:
    def __init__(self, qz):
        self.qz = qz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, width=400, height=600)
        self.canvas = Canvas(width=330, height=250)
        self.quest = self.canvas.create_text(150, 125, text=self.qz.next_question(), font=('Arial', 20, 'italic'),
                                             fill=THEME_COLOR, width=280)
        self.canvas.place(x=35, y=125)
        self.label = Label(text=f'Score: {self.qz.score}', bg=THEME_COLOR, fg='white', font=4)
        self.label.place(x=250, y=20)
        photoimage_right = PhotoImage(file=r'images\true.png')
        self.button_right = Button(image=photoimage_right, command=self.true_pressed)
        self.button_right.place(x=50, y=460)
        photoimage_wrong = PhotoImage(file=r'images\false.png')
        self.button_wrong = Button(image=photoimage_wrong, command=self.false_pressed)
        self.button_wrong.place(x=250, y=460)
        self.window.mainloop()

    def get_next_question(self):
        if not self.qz.still_has_questions():
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.quest,text="You've reached the end of the questions")
            self.button_right.config(state='disabled')
            self.button_wrong.config(state='disabled')
        else:
            self.canvas.config(bg='white')
            self.label.config(text=f'Score: {self.qz.score}')
            self.canvas.itemconfig(self.quest, text=self.qz.next_question())

    def true_pressed(self):
        is_right = self.qz.check_answer('True')
        self.feedback(is_right)

    def false_pressed(self):
        is_wrong = self.qz.check_answer('False')
        self.feedback(is_wrong)

    def feedback(self, right_wrong):
        if right_wrong:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

