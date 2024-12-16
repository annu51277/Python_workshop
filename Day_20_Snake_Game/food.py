# class Animal:
#     def __init__(self):
#         self.no_of_eyes = 10
#
#     def breathe(self):
#         print('Inhale and Exhale')
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#         self.no_of_eyes = 2
#
#     def swim(self):
#         print('Moving in Water')
#
#     def breathe(self):
#         super().breathe()
#         print("We are doing this under water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.no_of_eyes)
from turtle import Turtle
import random

class Food(Turtle): # Class Inheritance
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('blue')
        self.speed(0)
        random_x= random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        self.clear_food_move_food()


    def clear_food_move_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)

