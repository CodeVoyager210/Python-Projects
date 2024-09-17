from turtle import Turtle,Screen
from player import Player
from cars import car_manager
from scoreboard import scoreboard
import time
def move_up():
    global turtle
    turtle.move_player()
screen = Screen()
screen.title('Crossing Game')
screen.setup(width = 600,height= 600)
screen.tracer(0)
turtle = Player()
manage_cars = car_manager()
game_over = Turtle()
game_over.hideturtle()
game_over.color('black')
score = scoreboard()
loops = 0
screen.listen()
screen.onkey(move_up, 'w')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loops +=1
    if loops == 6:
        loops = 0
        manage_cars.create_car()
    manage_cars.move_cars()
    for car in manage_cars.all_cars:
        if turtle.distance(car) < 15:
            game_is_on = False
            game_over.goto(0, 0)
            game_over.write('Game Over!', align='center', font=('Arial', 20, 'normal'))
    if turtle.ycor() > 280:
        turtle.goto(0,-280)
        score.next_level()
        manage_cars.increase_speed()


screen.exitonclick()
