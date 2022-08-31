import turtle

SCORE_FONT = ('Arial', 50, 'normal')
END_FONT = ('Arial', 30, 'normal')
ALIGN = "center"

class ScoreBoard():

    penXY1 = (-200, 330)
    penXY2 = (200, 330)

    def __init__(self):
        self.pen1 = turtle.Turtle()
        self.pen1.color("white")
        self.pen1.hideturtle()
        self.pen1.penup()
        self.pen1.goto(ScoreBoard.penXY1)
        self.score1 = 0

        self.pen2 = turtle.Turtle()
        self.pen2.color("white")
        self.pen2.hideturtle()
        self.pen2.penup()
        self.pen2.goto(ScoreBoard.penXY2)
        self.score2 = 0

        self.writeScores()


    def incrementScore(self, xpos):
        if xpos > 0:
            self.score1 += 1
        else:
            self.score2 += 1

    def writeScores(self):
        self.clearScores()
        self.pen1.write(f"{self.score1}", align=ALIGN , font=SCORE_FONT)
        self.pen2.write(f"{self.score2}", align=ALIGN , font=SCORE_FONT)


    def clearScores(self):
        self.pen1.clear()
        self.pen2.clear()

    def win(self):

        if self.score1 < 10 and self.score2 < 10:
            return False

        endMessage1 = ""
        endMessage2 = ""
        if self.score1 > self.score2:
            endMessage1 = "WINNER"
            endMessage2 = "LOSER"
        else:
            endMessage1 = "LOSER"
            endMessage2 = "WINNER"

        self.clearScores()
        self.pen1.write(f"Player 1: {self.score1}\n   {endMessage1}", align=ALIGN , font=END_FONT)
        self.pen2.write(f"Player 2: {self.score2}\n   {endMessage2}", align=ALIGN , font=END_FONT)

        return True
