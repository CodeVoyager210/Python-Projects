from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_player(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
