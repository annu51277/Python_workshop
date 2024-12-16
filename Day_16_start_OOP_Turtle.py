from shutil import posix
from turtle import Turtle , Screen, color
zaidan=Turtle() # Turtle is class and () is used to activate the class and Zaidan is object name .
# print(zaidan)

my_screen = Screen() # my_screen is the object and screen() is the class.
print(zaidan.position())
my_screen.bgcolor("green")
zaidan.shape("turtle")
zaidan.color("Coral")
zaidan.pendown()
my_screen.title("Welcome to the turtle zoo!")
#
for i in range(0,4):
    zaidan.forward(100)
    zaidan.left(90)
    # zaidan.backward(100)
    zaidan.forward(100)

zaidan.penup()
zaidan.goto(210,0)
zaidan.pendown()
zaidan.pensize(5)
for j in range(0,3):
    zaidan.forward(100)
    zaidan.left(120)
    zaidan.forward(100)
# my_screen.clearscreen()

zaidan.penup()
zaidan.goto(-210,0)
zaidan.pendown()
zaidan.pensize(5)
zaidan.circle(50,360)

my_screen.exitonclick()
