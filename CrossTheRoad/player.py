import turtle

class Player(turtle.Turtle):
    defaultTurtleSize = 20
    stepSize = 10

    def __init__(self, size, startPos, shape, color):
        super().__init__(shape=shape)
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=size[0] / Player.defaultTurtleSize, stretch_wid=size[1] / Player.defaultTurtleSize)
        self.shapesize()
        self.goto(startPos)
        self.setheading(90)
        self.midToSideX = size[0] / 2
        self.midToSideY = size[1] / 2
        self.finishY = -startPos[1]


    def moveUp(self):
        self.goto(self.xcor(), self.ycor() + Player.stepSize)

    def collisionWithCar(self, car):
        px, py = self.pos()
        cx, cy = car.pos()
        if abs(float(px - cx)) < (self.midToSideX + car.midToSideX) and abs(float(py - cy)) < (self.midToSideY + car.midToSideY):
            return True
        return False

    def finish(self):
        if self.ycor() >= self.finishY:
            return True
        return False
