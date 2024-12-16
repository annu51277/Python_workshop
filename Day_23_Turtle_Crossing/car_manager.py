from turtle import Turtle
import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 50
MOVE_INCREMENT = 10
turtle.colormode(255)


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = 0.4

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=3,stretch_len=1)
        car.setheading(90)
        car.penup()
        car.color(self.car_color())
        y_cor = random.randint(-280,280)
        car.goto(280,y_cor)
        self.cars.append(car)
        return car


    def car_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        return rgb

    def car_move(self):
        for cars in self.cars:
            new_x = cars.xcor()-STARTING_MOVE_DISTANCE
            cars.goto(new_x,cars.ycor())

    def speed(self):
        self.car_speed *= 0.9