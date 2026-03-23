from turtle import Turtle


class CreateTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.setheading(90)
        self.penup()
        self.goToStart()

    def move(self):
        self.forward(20)

    def goToStart(self):
        self.goto(0, -280)