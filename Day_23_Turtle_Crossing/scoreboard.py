from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-230,250)
        self.write(f'Score:{self.score}',align='center',font=FONT)

    def score_board(self):
        self.score +=1
        self.clear()
        self.write(f'Score{self.score}', align='center', font=FONT)

    def game_over(self):
        self.color('black')
        self.goto(0,0)
        self.write('Game Over', align='Center', font=("Courier", 24, "normal"))
