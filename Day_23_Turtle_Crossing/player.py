from turtle import Turtle
import random
import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
turtle.colormode(255)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        self.color(rgb)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def win(self):
        self.write('Congratulations', align='Center', font=("Courier", 24, "normal"))
        self.clear()
        self.goto(STARTING_POSITION)