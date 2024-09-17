import colorgram
import random
from turtle import Turtle,Screen
import turtle

colors = colorgram.extract('spot.jpg', 11)

list_colors = []
for cl in range(11):
    all_colors = colors[cl]
    tp = tuple((all_colors.rgb.r,all_colors.rgb.b,all_colors.rgb.g))
    list_colors.append(tp)
screen = Screen()
screen.setworldcoordinates(-4, -4, screen.window_width() + 45, screen.window_height() + 4)
artist = Turtle()
turtle.colormode(255)
artist.speed(0)
artist.hideturtle()
screen.title('Hirst Spot Painting')

for loops in range(22):
    for paint in range(20):
        artist.penup()
        artist.forward(25)
        artist.dot(25, list_colors[random.randint(0, 10)])
        artist.forward(25)
        artist.pendown()
    artist.left(90)
    artist.penup()
    artist.forward(38)
    artist.left(90)
    artist.forward(1000)
    artist.right(90)
    artist.right(90)

screen.exitonclick()













