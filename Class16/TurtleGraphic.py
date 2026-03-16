import random
from turtle import Turtle,Screen   # Import class Turtle from module turtle

timmy=Turtle()   ##Object creation
my_screen = Screen()
timmy.shape("turtle")

def drawShapes(side):
    for _ in range(side):
        timmy.forward(100)
        angle=360/side
        timmy.right(angle)

colours=['red','blue','green','yellow','cyan']

for side in range(3,11):
        timmy.color(random.choice(colours))
        drawShapes(side)

my_screen.exitonclick()



