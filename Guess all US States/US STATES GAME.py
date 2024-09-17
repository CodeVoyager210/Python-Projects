from turtle import Screen, Turtle

import pandas
import turtle
data = pandas.read_csv('50_states.csv')
data_dict = data.to_dict(orient='records')
image = 'blank_states_img.gif'
score = 0
r = 0
screen = Screen()
screen.setup(725,491)
screen.addshape(image)
turtle.shape(image)
box = turtle.textinput(f'{score}/50 States Correct', "What's another state name?")
capital = box.title()
game_is_on = True
while game_is_on:
    for s in data_dict:
        if capital == s['state']:
            r +=1
            score += 1
            st = Turtle()
            st.hideturtle()
            st.penup()
            st.goto(s['x'], s['y'])
            st.write(s['state'])
            turtle.clear()
            box = turtle.textinput(f'{score}/50 States Correct', "What's another state name?")
            capital = box.title()
    if capital not in list(data['state']):
        r +=1
        turtle.clear()
        box = turtle.textinput(f'{score}/50 States Correct', "What's another state name?")
        capital = box.title()
    if r == 50:
        game_is_on = False
print(f'You got {score} out of 50')






