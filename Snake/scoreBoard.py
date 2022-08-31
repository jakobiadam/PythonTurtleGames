import turtle


SCORE_COLOR = "green"
GAME_OVER_COLOR = "red"
HIGH_SCORES_COLOR = "white"
PLAYER_SCORE_COLOR = "yellow"
RESTART_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Arial', 30, 'normal')
HIGH_SCORES_FONT = ('Arial', 20, 'normal')

class ScoreBoard():
    scorePenPos = [0, 250]
    gameOverPos = [0, 210]
    highScoresPos = [[0, i] for i in range(150, -149, -30)]
    restartPenPos = [0, -200]

    def __init__(self):
        self.scorePen = self.createPen(ScoreBoard.scorePenPos, SCORE_COLOR)
        self.gameOverPen = self.createPen(ScoreBoard.gameOverPos, GAME_OVER_COLOR)
        self.highScorePens = self.create10Pens(ScoreBoard.highScoresPos, HIGH_SCORES_COLOR)
        self.restartPen = self.createPen(ScoreBoard.restartPenPos, RESTART_COLOR)
        self.score = 0

    def incrementScore(self, point):
        self.score += point

    def writeScore(self):
        self.scorePen.clear()
        self.scorePen.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.gameOverPen.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def clearGameOver(self):
        self.gameOverPen.clear()

    def writeRestart(self):
        self.restartPen.write("Press Enter to restart", align=ALIGNMENT, font=FONT)

    def clearRestart(self):
        self.restartPen.clear()

    def createPen(self, pos, color):
        pen = turtle.Turtle()
        pen.color(color)
        pen.hideturtle()
        pen.penup()
        pen.goto(pos)
        pen.pendown()
        return pen

    def create10Pens(self, posList, color):
        pens = []
        for pos in posList:
            pens.append(self.createPen(pos, color))
        return pens

    def clear10Pens(self):
        for pen in self.highScorePens:
            pen.color(HIGH_SCORES_COLOR)
            pen.clear()

    def writeHighScore(self, name):
        placeIndex = 11
        highScores = []
        with open("highScores.txt", "r") as f:
            for _ in range(10):
                line = f.readline().split('\t')
                highScores.append([line[0], int(line[1])])
        for i in range(10):
            if self.score > highScores[i][1]:
                highScores.insert(i, [name, self.score])
                placeIndex = i
                break

        with open("highScores.txt", "w") as f:
            for i in range(10):
                f.write(f"{highScores[i][0]}\t{highScores[i][1]}\n")

        for i in range(10):
            if i == placeIndex:
                self.highScorePens[i].color(PLAYER_SCORE_COLOR)
            self.highScorePens[i].write(f"{highScores[i][0]}\t{highScores[i][1]}", align=ALIGNMENT, font=HIGH_SCORES_FONT)

    def startNewGame(self):
        self.clear10Pens()
        self.clearGameOver()
        self.clearRestart()
        self.score = 0
        self.writeScore()