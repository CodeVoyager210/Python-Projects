from turtle import Turtle, Screen
import time
import turtle

screen = Screen()
screen.setup(width=800, height=650)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
net = Turtle()
net.color('white')
net.pensize(width=5)
net.hideturtle()
net.penup()
net.goto(0, 300)
net.setheading(270)
starting_points = [(-350, 0), (350, 0)]
starting_points_score = [(-100,200),(100,200)]
players = []
scoreboard = []
score_l = 0
score_r = 0
for _ in range(19):
    net.pendown()
    net.forward(15)
    net.penup()
    net.forward(15)
for p in range(2):
    player = Turtle()
    player.shape('square')
    player.color('white')
    player.shapesize(stretch_wid=5, stretch_len=1)
    player.penup()
    player.goto(starting_points[p - 1])
    players.append(player)
for s in range(2):
    score = Turtle()
    score.color('white')
    score.penup()
    score.hideturtle()
    score.goto(starting_points_score[s -1])
    scoreboard.append(score)
scoreboard[0].write(score_r,align='center',font =('Courier',80,'normal'))
scoreboard[1].write(score_l,align='center',font=('Courier',80,'normal'))


def move_up_p1():
    new_y = players[1].ycor() + 30
    players[1].goto(players[1].xcor(), new_y)


def move_down_p1():
    new_y = players[1].ycor() - 30
    players[1].goto(players[1].xcor(), new_y)


def move_up_p2():
    new_y = players[0].ycor() + 30
    players[0].goto(players[0].xcor(), new_y)


def move_down_p2():
    new_y = players[0].ycor() - 30
    players[0].goto(players[0].xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_posistion(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1
    def ball_reset(self):
        self.goto(0,0)
        self.ball_bounce_x()

game_is_on = True
starting_ball = Ball()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard[0].write(score_r, align='center', font=('Courier', 80, 'normal'))
    scoreboard[1].write(score_l, align='center', font=('Courier', 80, 'normal'))
    starting_ball.ball_posistion()
    if starting_ball.ycor() > 300 or starting_ball.ycor() < -300:
        starting_ball.ball_bounce_y()
    if starting_ball.distance(players[0]) < 40 and starting_ball.xcor() > 300 or starting_ball.distance(players[1]) < 40 and starting_ball.xcor() < -300:
        starting_ball.ball_bounce_x()
    if starting_ball.xcor() > 380:
        starting_ball.ball_reset()
        score_l += 1
        scoreboard[1].clear()
    if starting_ball.xcor() < -380:
        starting_ball.ball_reset()
        score_r += 1
        scoreboard[0].clear()
    screen.listen()
    screen.onkey(move_up_p1, 'w')
    screen.onkey(move_down_p1, 's')
    screen.onkey(move_up_p2,'Up')
    screen.onkey(move_down_p2,'Down')

screen.exitonclick()
