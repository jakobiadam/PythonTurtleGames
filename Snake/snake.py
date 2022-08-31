import turtle
from queue import Queue

class Snake:
    startingPositions = [(-40, 0), (-20, 0), (0, 0)]

    def __init__(self):
        self.snake = Queue(maxsize=1000)
        self.startSnake()

    def newPart(self, pos):
        part = turtle.Turtle(shape="square")
        part.penup()
        part.color("gray")
        part.setpos(pos)
        return part

    def startSnake(self):
        self.turnState = "right"
        for i in range(3):
            self.snake.put(self.newPart(Snake.startingPositions[i]))

    def w(self):
        if self.turnState != "down":
            self.turnState = "up"

    def s(self):
        if self.turnState != "up":
            self.turnState = "down"

    def a(self):
        if self.turnState != "right":
            self.turnState = "left"

    def d(self):
        if self.turnState != "left":
            self.turnState = "right"

    def move(self):
        self.moveHead()
        part = self.snake.get()
        part.clear()
        part.hideturtle()
        del(part)

    def moveTail(self):
        self.moveHead()

    def moveHead(self):

        if self.turnState == "left" and self.snake.queue[-1].xcor() <= -300:
            self.snake.put(self.newPart((300, self.snake.queue[-1].ycor())))

        elif self.turnState == "left":
            self.snake.put(self.newPart((self.snake.queue[-1].xcor() - 20, self.snake.queue[-1].ycor())))

        elif self.turnState == "right" and self.snake.queue[-1].xcor() >= 300:
            self.snake.put(self.newPart((-300, self.snake.queue[-1].ycor())))

        elif self.turnState == "right":
            self.snake.put(self.newPart((self.snake.queue[-1].xcor() + 20, self.snake.queue[-1].ycor())))

        elif self.turnState == "up" and self.snake.queue[-1].ycor() >= 300:
            self.snake.put(self.newPart((self.snake.queue[-1].xcor(), -300)))

        elif self.turnState == "up":
            self.snake.put(self.newPart((self.snake.queue[-1].xcor(), self.snake.queue[-1].ycor() + 20)))

        elif self.turnState == "down" and self.snake.queue[-1].ycor() <= -300:
            self.snake.put(self.newPart((self.snake.queue[-1].xcor(), 300)))

        elif self.turnState == "down":
            self.snake.put(self.newPart((self.snake.queue[-1].xcor(), self.snake.queue[-1].ycor() - 20)))

    def testCollision(self):
        for i in range(0, len(self.snake.queue) - 1):
            if self.snake.queue[i].pos() == self.snake.queue[-1].pos():
                return True
        else:
            return False

    def foodCollision(self, food):
        if (self.snake.queue[-1]).pos() == food.pos():
            return True
        else:
            return False

    def newSnake(self):

        while len(self.snake.queue) > 0:
            part = self.snake.get()
            part.clear()
            part.hideturtle()
            del(part)

        self.startSnake()