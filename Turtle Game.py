from turtle import Screen, Turtle
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title('Turtle Racing Game')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
while True:
    if user_bet not in colors:
        user_bet = screen.textinput(title='Make your bet', prompt='Please enter a color')
    else:
        break
all_turtles = []
y_positions = [-70,-40,-10,20,50,80]
for turtles_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtles_index])
    new_turtle.goto(x=-230, y=y_positions[turtles_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for_loop = False
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                for_loop = True
                print(f'You win the {turtle.pencolor()} turtle won the race')
                break
            else:
                for_loop = True
                print(f'You lost {turtle.pencolor()} turtle won the race')
                break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    if for_loop:
        break
screen.exitonclick()


