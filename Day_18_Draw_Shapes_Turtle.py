import turtle
from random import random
from turtle import Turtle,Screen
import random


tim = Turtle()
screen = Screen()
tim.shape("turtle")
turtle.colormode(255)

# This is for Square
# for i in range(0,4):
#     tim.forward(100)
#     tim.left(90)
#
#   This is for dotted lines ###########
# for i in range(0,15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# tim.penup()
# tim.goto(-70, 0)
# tim.left(180)
# for i in range(0,15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

############


### Draw a triangle , Square , Pentagon , hexagon , Heptagon , octagon , Nonagon , decagon

colors = ["red","blue","green","purple","yellow","orange","cyan","magenta","pink","brown","light blue",
            "lime",  "navy","gold","teal","violet","coral","salmon","indigo","crimson"]

def color_tim():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = ( r,g,b )
    return rgb

tim.pensize(3)


def draw_shapes(no_of_sides):
    angle = 360/no_of_sides
    tim.pencolor(color_tim())

    for j in range(no_of_sides):
        tim.forward(100)
        tim.left(angle)

for i in range(3,12):
    draw_shapes(i)


def draw_shapes(no_of_sides):
    angle = 360/no_of_sides
    tim.pencolor(color_tim())
    for i in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,12):
    draw_shapes(i)


screen.exitonclick()


