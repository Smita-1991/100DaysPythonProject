import random
from turtle import *

screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_color=['Red','Blue','Green',"Yellow",'Purple','gray','pink']
turtle_name=['timmy','toca','bobo','lolo','momo','moka','roka']
turtle_speed=[1,2,3,4,5,6,7]
turtle_list=[]
x_axis = -235
y_axis = -180


for i in range(7):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(turtle_color[i])
    turtle.goto(x_axis,y_axis)
    y_axis += 50
    turtle_list.append(turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    random_turtle=random.choice(turtle_list)
    random_turtle.forward(random.choice(turtle_speed))
    if random_turtle.xcor()>230:
        is_race_on=False
        if user_bet==random_turtle.color():
            print(f"You won")
        else:
            print(f"You lost and the winner is :{random_turtle.color()[0]}")
screen.exitonclick()
