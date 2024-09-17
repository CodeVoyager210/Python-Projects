from turtle import Turtle
level = 0
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.write(f'Level: {level}',align='left',font=('Arial',13,'normal'))
    def next_level(self):
        global level
        level +=1
        self.clear()
        self.write(f'Level: {level}', align='left', font=('Arial', 13, 'normal'))

