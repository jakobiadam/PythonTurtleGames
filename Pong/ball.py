import turtle
import random
import numpy as np

class Ball(turtle.Turtle):

    stampSize = 20
    movingUnit = 10
    decreaseAngle = 1.5

    def __init__(self, size, xmin, xmax, ymin, ymax):
        super().__init__(shape="circle")
        self.shapesize(stretch_wid=(size / Ball.stampSize), stretch_len=(size / Ball.stampSize))
        self.penup()
        self.color("white")
        self.start()
        self.size = size
        self.xmin = xmin + size / 2
        self.xmax = xmax - size / 2
        self.ymin = ymin + size / 2
        self.ymax = ymax - size / 2

    def move(self):
        self.forward(Ball.movingUnit)

    def start(self):
        self.goto(0,0)
        self.setheading((random.randint(-30, 30) + random.choice([0, 180])) % 360)

    def collisionSide(self):
        y = self.ycor()
        if (y <= self.ymin) or (y >= self.ymax):
            return True
        return False

    def collisionBorder(self):
        x = self.xcor()
        if (x <= self.xmin) or (x >= self.xmax):
            return True
        return False

    def collisionPaddle(self, paddle):
        ballX, ballY = self.pos()
        paddleX, paddleY = paddle.pos()
        if abs(float(ballX - paddleX)) <= ((paddle.xlength + self.size) / 2) and abs(float(ballY - paddleY)) <= ((paddle.ylength + self.size) / 2):
            return True

    def bounceSide(self):
        self.setheading(360 - self.heading())

    def bouncePaddle(self, paddle, frame_delay_ms):
        ballX, ballY = self.pos()
        paddleX, paddleY = paddle.pos()
        alpha = 0
        try:
            alpha = np.arctan(abs(float(ballY - paddleY)) / abs(float(ballX - paddleX))) * 180 / 3.14 / self.decreaseAngle
        except:
            pass

        if (paddleX < ballX):
            if (paddleY <= ballY):
                self.setheading(alpha)
            elif (paddleY > ballY):
                self.setheading(360 - alpha)
        elif (paddleX > ballX):
            if (paddleY <= ballY):
                self.setheading(180 - alpha)
            elif (paddleY > ballY):
                self.setheading(180 + alpha)
        else:
            self.setheading((-self.heading()) % 360)

        return int(0.95 * frame_delay_ms)

    

