import random
import time
from turtle import Screen
from Game.TurtleCrossingGame.Car import Car
from Game.TurtleCrossingGame.GameStatus import GameStatus
from Game.TurtleCrossingGame.TurtleCross import CreateTurtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("White")
screen.title("Turtle Crossing Game")
screen.tracer(0)

createTurtle = CreateTurtle()
car=Car()
gameStatus = GameStatus()
screen.listen()
screen.onkey(createTurtle.move, "Up")
level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.35)
    screen.update()
    gameStatus.gameLevel(level)
    if level == 3:
        screen.clear()
        gameStatus.gameWin()
    else:
        for i in range(random.randint(1, 6)):
            if i==1:
                car.createCars()
        car.move_car()

        #Detect collision with the car
        for new_car in car.newCar:
            if createTurtle.distance(new_car)<20:
                game_is_on = False
                screen.clear()
                gameStatus.gameOver()
            elif createTurtle.ycor()>280:
                level+= 1
                createTurtle.goToStart()


screen.exitonclick()