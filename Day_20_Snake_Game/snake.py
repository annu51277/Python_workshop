from turtle import  Turtle

SNAKE_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE= 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.set_head = self.snake[0]


    def create_snake(self):
        for sqr in SNAKE_POSITIONS:
            duck = Turtle("circle")
            duck.color("pink")
            duck.penup()
            duck.goto(sqr)
            self.snake.append(duck)

    def extend(self):
        duck = Turtle("circle")
        duck.penup()
        duck.goto(self.snake[-1].position())
        duck.color('pink')
        self.snake.append(duck)


    def move(self):
        for position in range(len(self.snake) - 1, 0,-1):   # This is tricky and when you come after long time you will get confuse .
                                                            # We want to move our snake body to goto the square in front  of it .
                                                            # It means we only move head and just switch places of other squares.
                                                            # Snake[0] will move forward and snake[2] takes position of snake[1] and snake[1] takes position of snake[0] .
                                                            # It is done with range() function . range(start=3, stop=0, steps=-1) . It means it goes backwards
            new_x = self.snake[position - 1].xcor()
            new_y = self.snake[position - 1].ycor()
            self.snake[position].goto(new_x, new_y)
        self.snake[0].fd(MOVE_DISTANCE)

    def move_up(self):
        if self.set_head.heading() != DOWN:
            self.set_head.setheading(90)
    def move_down(self):
        if self.set_head.heading() != UP:
            self.set_head.setheading(270)
    def move_lt(self):
        if self.set_head.heading() != RIGHT:
            self.set_head.setheading(180)
    def move_rt(self):
        if self.set_head.heading() != LEFT:
            self.set_head.setheading(0)

    def snake_die(self):
        for i in self.snake:
            i.color('white')
            i.goto(0,0)
            i.write(f'Game Over', False, "center", ("Verdana", 15, 'normal'))
