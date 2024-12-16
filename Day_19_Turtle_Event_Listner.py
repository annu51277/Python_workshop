from turtle import Turtle , Screen

mickey = Turtle()
tommy = Turtle()
screen = Screen()

mickey.shape("turtle")
mickey.color("blue")
def turn_right():
    new_heading = mickey.heading() - 10
    mickey.setheading(new_heading)
def move_forward():
    mickey.fd(20)
def move_back():
    mickey.bk(20)
def turn_left():
    new_heading = mickey.heading() + 10
    mickey.setheading(new_heading)

def clear_screen():
    mickey.clear()
    mickey.reset()

screen.listen()
screen.onkey(key="Up",fun=turn_right)
screen.onkey(key="Right",fun=move_forward)
screen.onkey(key="Left",fun=move_back)
screen.onkey(key="Down",fun=turn_left)
screen.onkey(key="c",fun=clear_screen)



screen.exitonclick()

