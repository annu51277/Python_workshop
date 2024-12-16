import  pandas as pd
from turtle import Turtle , Screen



class States(Turtle):
    def __init__(self):
        super().__init__()
        screen = Screen()
        self.u_guess = screen.textinput('Guess', 'State Name ?')
        self.states = pd.read_csv('50_states.csv')

    def move(self):
        state = self.states[self.states['state'] == self.u_guess]
        state['x']

