import random
import time
from turtle import Turtle,Screen

from Day20.Food import Food
from Day20.ScoreBoard import Scoreboard
from Snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreBoard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increase_score()
        snake.extendSnake()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.game_over()
        game_is_on = False

    #Detect collision with the body
    for seg in snake.segments[1:]:
       if seg.distance(snake.head) < 10:
            scoreBoard.game_over()
            game_is_on = False









