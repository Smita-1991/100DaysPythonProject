from turtle import Turtle


class GameStatus(Turtle):
    def __init__(self):
        super().__init__()

    def gameOver(self):
        self.clear()
        self.fillcolor("Red")
        self.write("GAME OVER", move=False, align='center', font=('Arial', 15, 'normal'))

    def gameWin(self):
        self.clear()
        self.write("YOU ARE WINNER", move=False, align='center', font=('Arial', 15, 'normal'))

    def gameLevel(self,level):
        self.clear()
        self.write(f"LEVEL {level}", move=False, align='center', font=('Arial', 15, 'normal'))


