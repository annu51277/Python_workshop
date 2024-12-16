from turtle import Screen
import time

from snake import Snake
from food import Food
from scorebord import ScoreBoard

screen = Screen()

screen.setup(width=800,height=800)
screen.bgcolor("black")
snake_position = [(0,0),(-20,0),(-40,0)]
screen.tracer(0) # By setting screen.tracer(0), the program stops automatically updating the screen every time a change is made (like moving a turtle).
                 # Instead, it requires you to manually call screen.update() to refresh the display.
                 #   This gives you complete control over when the screen updates.

snake = Snake()
food  = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key='Down',fun=snake.move_down)
screen.onkey(key='Right',fun=snake.move_rt)
screen.onkey(key='Left',fun=snake.move_lt)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    for i in snake.snake[1:]:
        if snake.set_head.distance(i)<10:
            snake.snake_die()
            score.h_score()
            is_game_on = False
    # Detection with collision with food
    # turtle.distance(x, y=None) Return the distance from the turtle to(x, y), the  given vector, or the given other  turtle, in turtle step units.
    if snake.set_head.distance(food) < 15:
        food.clear_food_move_food()
        snake.extend()
        score.score_new()

    if snake.set_head.xcor() >=398 or snake.set_head.xcor() <=-390 or snake.set_head.ycor() >=398 or snake.set_head.ycor() <=-398 :
        snake.snake_die()
        score.h_score()
        is_game_on = False


screen.exitonclick()
