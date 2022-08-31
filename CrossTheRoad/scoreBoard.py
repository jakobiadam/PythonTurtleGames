import turtle

LEVEL_FONT = ('Arial', 30, 'normal')
GAME_OVER_FONT = ('Arial', 50, 'bold')

class ScoreBoard(turtle.Turtle):

    def __init__(self, levelPos):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(levelPos)
        self.level = 0

    def incrementLevel(self):
        self.level += 1

    def writeNewLevel(self):
        self.clear()
        self.incrementLevel()
        self.write(f"Level: {self.level}", align="left", font=LEVEL_FONT)

    def writeGameOver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=GAME_OVER_FONT)