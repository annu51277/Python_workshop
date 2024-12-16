import turtle
from turtle import Turtle, Screen
import random

# Create the turtle and screen objects
jim = Turtle()
screen = Screen()
turtle.colormode(255)

# Define angles and directions
angles = [0, 90, 180, 270]
steps = 15
shape = ["turtle","arrow","circle"]

# Set the pen size
jim.pensize(5)
jim.speed(0)

def color_tim():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

# Move the turtle
for _ in range(600):  # Change this number for more steps
    angle = random.choice(angles)
    jim.setheading(angle)  # Set the turtle's direction to a random angle
    jim.pencolor(color_tim())
    jim.shape(random.choice(shape))# To change the random color
    jim.forward(steps)  # Move the turtle forward by the defined steps

# Finish up
screen.mainloop()  # Keep the window open
