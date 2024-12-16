import turtle
from turtle import Turtle , Screen
import random

tom = Turtle()
screen = Screen()
turtle.colormode(255)
tom.speed(0)
tom.pensize(1)

def color_tim():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb


def draw_circles(steps):
    for _ in range(int(360/steps)):
        tom.color(color_tim())
        tom.circle(100)
        tom.left(steps)

draw_circles(1)
screen.exitonclick()


