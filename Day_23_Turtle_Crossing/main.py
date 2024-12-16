import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Car Crossing')

player =  Player()

car = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()
    # Creating the cars and moving them across the screen.
    car.create_car()
    car.car_move()

## Collision with turtle
    for i in car.cars:
        if i.distance(player) < 30 : # My car is 20 pixels in height and 60 pixes in length.
            score_board.game_over()
            game_is_on = False

    ## Winning the race
    if player.ycor() > 260:
        score_board.score_board()
        player.win()
        car.speed()



screen.exitonclick()