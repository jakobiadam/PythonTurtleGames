import turtle
import random

X_RANGE = (-300, 301, 20)
Y_RANGE = (-300, 301, 20)

class Food(turtle.Turtle):

    colors = ["blue", "green", "red"]
    xPos = [i for i in range(X_RANGE[0], X_RANGE[1], X_RANGE[2])]
    yPos = [i for i in range(Y_RANGE[0], Y_RANGE[1], Y_RANGE[2])]

    def __init__(self):
        super().__init__(shape = "circle")
        self.penup()
        self.changePosition()

    def changePosition(self):
        self.setpos(random.choice(self.xPos), random.choice(self.yPos))
        index = random.randint(0,2)
        self.color(Food.colors[index])
        self.point = index + 1
