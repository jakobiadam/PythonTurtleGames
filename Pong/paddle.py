import turtle

class Paddle(turtle.Turtle):

    stampSize = 20
    movingUnit = 10

    def __init__(self, size, startingPos, ymax, ymin):
        super().__init__(shape="square")
        self.shapesize(stretch_len=(size[0] / Paddle.stampSize), stretch_wid=(size[1] / Paddle.stampSize))
        self.penup()
        self.color("white")
        self.goto(startingPos)
        self.xlength = size[0]
        self.ylength = size[1]
        self.ymax = ymax - size[1] / 2
        self.ymin = ymin + size[1] / 2

    def moveUp(self):
        x, y = self.pos()
        if (y < self.ymax):
            self.goto(x, min(y + Paddle.movingUnit, self.ymax))

    def moveDown(self):
        x, y = self.pos()
        if (y > self.ymin):
            self.goto(x, max(y - Paddle.movingUnit, self.ymin))