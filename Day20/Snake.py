from turtle import Turtle,Screen
import time

SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN=270
UP=90
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]


    def createSnake(self):
        for pos in SEGMENT_POSITION:
           self.add_snake(pos)

    def add_snake(self,position):
        new_seg = Turtle()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extendSnake(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                x_cor=self.segments[seg_num-1].xcor()
                y_cor=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(x_cor,y_cor)
            self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading!=LEFT:
            self.head.setheading(RIGHT)
