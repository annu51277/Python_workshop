from turtle import Turtle


class ScoreBoard(Turtle):  #Class Inheritance
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 380)
        self.score = 0
        with open('C:/Users/ansar/OneDrive/Desktop/data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.write(f'Score:{self.score} High Score: {self.high_score}', False, "center", ("Verdana", 15, 'normal'))

    def score_new(self):
        self.score += 1
        self.clear()
        self.write(f'Score:{self.score} High Score: {self.high_score}', False, "center", ("Verdana", 15, 'normal'))

    # C:\Users\ansar\OneDrive\Desktop
    def h_score(self):
        if self.score > self.high_score:
            # self.high_score = self.score
            with open('C:/Users/ansar/OneDrive/Desktop/data.txt', mode='w') as data:
                data.write(str(self.score))
            self.clear()
            self.write(f'Score:{self.score} High Score: {self.high_score}', False, "center", ("Verdana", 15, 'normal'))
        self.score = 0
