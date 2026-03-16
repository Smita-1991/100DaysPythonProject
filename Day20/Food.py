import random
from turtle import Turtle

from Day20.Snake import Snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("Blue")



    def refresh(self):
        random_x = random.randrange(-280, 280)
        random_y = random.randrange(-280, 280)
        self.goto(random_x, random_y)

