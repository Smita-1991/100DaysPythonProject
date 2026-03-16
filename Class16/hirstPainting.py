import random

import colorgram
import turtle as t

screen = t.Screen()
screen.colormode(255)
rgb_color = []
t.hideturtle()


image_colours=colorgram.extract("image.jpg",50)
print(image_colours)
for color in image_colours:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.r
    color=(r,g,b)
    rgb_color.append(color)

print(rgb_color)
dot_count=100

for number in range(1,dot_count):
    t.dot(20, random.choice(rgb_color))
    t.penup()
    t.forward(50)

    if number % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



screen.exitonclick()

