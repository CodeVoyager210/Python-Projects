from turtle import Turtle
import random
import time

colors = ['green', 'red', 'yellow', 'orange', 'blue']




class car_manager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 10
    def create_car(self):
        new_car = Turtle(shape= 'square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(colors))
        random_y = random.randint(-250,250)
        new_car.goto(320,random_y)
        self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def increase_speed(self):
        self.car_speed +=4



