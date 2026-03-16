import random
from turtle import *

turtle=Turtle()
screen = Screen()
screen.colormode(255)

turtle.speed(0)
size_of_gap=5

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    r_color=(r,g,b)
    return r_color

for _ in range(100):
    turtle.color(random_color())
    turtle.circle(50)
    current_heading=turtle.heading()
    turtle.setheading(current_heading+size_of_gap)

screen.exitonclick()