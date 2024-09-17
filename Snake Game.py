from turtle import Turtle, Screen
import time
import random
import turtle

screen = Screen()
screen.title('Snake')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
starting_points = [(0, 0), (-20, 0), (-40, 0)]
snakes = []
score = 0


def move_up():
    snakes[0].setheading(90)


def move_left():
    snakes[0].setheading(180)


def move_right():
    snakes[0].setheading(0)


def move_down():
    snakes[0].setheading(270)


def random_food():
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    food.goto(random_x, random_y)


def create_snake():
    for position in starting_points:
        add_segment(position)
def add_segment(position):
    snake = Turtle(shape='square')
    snake.color('white')
    snake.penup()
    snake.goto(position)
    snakes.append(snake)

create_snake()
game_is_on = True
food = Turtle(shape='circle')
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.color('blue')
food.speed('fastest')
random_food()
while game_is_on:
    scoreboard = turtle
    scoreboard.hideturtle()
    scoreboard.color('white')
    scoreboard.penup()
    scoreboard.goto(0, 270)
    scoreboard.write(f'Score: {score}', align='center', font=('Arial', 20, 'normal'))
    screen.update()
    time.sleep(0.1)
    for snakes_num in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snakes_num - 1].xcor()
        new_y = snakes[snakes_num - 1].ycor()
        snakes[snakes_num].goto(new_x, new_y)
    snakes[0].forward(20)
    screen.listen()
    screen.onkey(move_up, 'w')
    screen.onkey(move_left, 'a')
    screen.onkey(move_right, 'd')
    screen.onkey(move_down, 's')

    if snakes[0].distance(food) < 15:
        add_segment(snakes[-1].position())
        scoreboard.clear()
        random_food()
        score += 1
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
        game_is_on = False
        game_over = turtle
        game_over.color('white')
        game_over.goto(0, 0)
        game_over.write('Game Over', align='center', font=('Arial', 20, 'normal'))
        screen.exitonclick()
    for collision in snakes:
        if collision == snakes[0]:
            pass
        elif snakes[0].distance(collision) < 10:
            game_is_on = False
            game_over = turtle
            game_over.color('white')
            game_over.goto(0, 0)
            game_over.write('Game Over', align='center', font=('Arial', 20, 'normal'))
            screen.exitonclick()
