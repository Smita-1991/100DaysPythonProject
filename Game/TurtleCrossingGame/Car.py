import random
from turtle import Turtle

color=['red','blue','green','yellow','cyan','magenta','pink']

class Car:
    def __init__(self):
        self.newCar=[]

    def createCars(self):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color(random.choice(color))
        turtle.shapesize(1, 2, 1)
        turtle.penup()
        x_cor = 380
        y_cor = random.randint(-200, 280)
        turtle.goto(x_cor, y_cor)
        self.newCar.append(turtle)

    def move_car(self):
        for car in self.newCar:
            car.backward(20)

