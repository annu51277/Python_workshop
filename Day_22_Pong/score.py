from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(pos)
        self.score = 0
        self.write(f'Score:0', False, "center", ("Verdana", 15, 'normal'))

    def score_r(self) :
        self.score += 1
        self.clear()
        self.write(f'Score:{self.score}', False, "center", ("Verdana", 15, 'normal'))


    def score_l(self) :
        self.score += 1
        self.clear()
        self.write(f'Score:{self.score}', False, "center", ("Verdana", 15, 'normal'))


