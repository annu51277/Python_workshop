from turtle import Turtle

class Pong(Turtle):

    def __init__(self,position_turtle):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position_turtle)

    def move_up(self):
            y_cor = self.ycor()+10
            self.goto(self.xcor(),y_cor)

    def move_down(self):
            y_cor = self.ycor()-10
            self.goto(self.xcor(),y_cor)

