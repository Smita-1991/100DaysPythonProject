import random
from turtle import *

turtle=Turtle()
turtle.shape("turtle")
turtle.pensize(15)
turtle.speed(0)
my_screen = Screen()
my_screen.colormode(255)

length=2
angle=90

colours=['red','blue','green','yellow','cyan']
directions=[0,90,180,270]


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    randomColor=(r,g,b)
    return randomColor

for _ in range(100):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))


my_screen.exitonclick()
