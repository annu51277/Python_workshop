import turtle


from colorgram import colorgram

# color gram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

rgb_colors_extract = []

def hirst_colors(no_of_colors):
    colors = colorgram.extract('image-2.jpg', no_of_colors)

    for i in colors:

        r = i.rgb.r # e.g. (255, 151, 21  0)
        g = i.rgb.g
        b = i.rgb.b # e.g. (230, 255, 203)
        rgb = (r,g,b)
        rgb_colors_extract.append(rgb)
    return rgb_colors_extract

colors_new = hirst_colors(50)
print(colors_new)

from turtle import Turtle , Screen
import random

turtle.colormode(255)
jerry = Turtle()
screen = Screen()
jerry.pensize(20)
jerry.hideturtle()


def rows_columns(steps):
    jerry.penup()
    jerry.setpos(-250, -250)
    # jerry.pendown()
    def no_of_dots():
        for __ in range(steps):
            jerry.dot(20,random.choice(colors_new) )
            jerry.penup()
            jerry.fd(50)
    for _ in range(steps):
        no_of_dots()
        position = jerry.pos()[1]+50
        jerry.setpos(-250,position)
        print(jerry.pos()[1])

rows_columns(10)


screen.exitonclick()







