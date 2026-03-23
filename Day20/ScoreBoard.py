from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highScore.txt","r") as file:
            self.highScore = int(file.read())
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Score={self.score}  HighScore={self.highScore}",align="center",font=("Arial",15,"bold"))
        return self.highScore

    def resetScore(self):
        if self.score>self.highScore:
            self.highScore = self.score
            with open("highscore.txt", "w") as file:
                file.writelines(f"{self.highScore}")
        self.score=0
        self.update_scoreBoard()

    def increase_score(self):
        self.score+=1
        self.update_scoreBoard()






    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER",align="center",font=("Arial",15,"bold"))
