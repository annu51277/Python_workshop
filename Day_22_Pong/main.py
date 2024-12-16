import time
from turtle import  Screen

from pong import Pong

from ball import Ball

from score import ScoreBoard

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

r_paddle = Pong((380,0))
l_paddle = Pong((-380,0))

ball = Ball()

score_r = ScoreBoard((280,280))
score_l = ScoreBoard((-280,280))

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball needs to bounce
        ball.ball_bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()


    # if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
    #     score_r.score_r()
    #
    # if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
    #     score_l.score_l()

    if ball.xcor() > 390 :
        ball.reset()
        score_l.score_l()


    if ball.xcor() < -390:
        ball.reset()
        score_r.score_r()






screen.exitonclick()