import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
colors = ["red","orange","yellow","green","blue","purple"]


screen.setup(width=1000,height=800,startx=100,starty=10)
coordinates = (-490,50)
position = []
racing_turtles = []

def turtles():
    for __ in range(0,6):
        jeff__ = Turtle()
        jeff__.shape("turtle")
        jeff__.penup()
        jeff__.color(colors[__])
        position.append(coordinates[1] * __ )
        jeff__.goto(coordinates[0],position[__])
        racing_turtles.append(jeff__)

def start_race(race):
    winner = None
    finish_line = 460  # X-coordinate for the finish line

    while not winner:
        for jeff in racing_turtles:
            jeff.forward(random.randint(10, 25))
            # Check if this turtle has crossed the finish line
            if jeff.xcor() > finish_line:
                winner = jeff.pencolor()
                break

    return winner
turtles() # This will align the turtles to their positions .

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race and enter a color: ?")

winning_color = start_race(racing_turtles) # racing_turtle is global ,


result = Turtle() # This is created for winner/looser dialog popup


if user_bet == winning_color:
    result.write(f'Congratulations! Your {winning_color} turtle won!', font=("Arial", 16, "normal") , align='center')
else:
    result.write(f"Sorry, the {winning_color} turtle won. Better luck next time!",font=("Arial", 16, "normal") , align='center')

screen.exitonclick()