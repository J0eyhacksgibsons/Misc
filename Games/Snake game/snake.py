from turtle import Turtle
import time
STARTING_Positions = [(0,0), (-20,0), (-40,0)]
Move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
    def create_snake(self):
        for position in STARTING_Positions:
           self.add_square(position)
    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("green")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)
    def extend(self):
        self.add_square(self.squares[-1].position())
    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):    
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x,new_y)
        self.squares[0].forward(Move_distance)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            time.sleep(0.01)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            time.sleep(0.01)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            time.sleep(0.01)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            time.sleep(0.01)

    def reset(self):
        for square in self.squares:
            square.goto(10000,10000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]