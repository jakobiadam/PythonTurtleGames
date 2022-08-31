import turtle
import random

class Car(turtle.Turtle):
    defaultTurtleSize = 20
    stepSize = 10
    colors = ["red", "green", "blue", "brown", "black", "white", "yellow", "purple"]

    def __init__(self, size, startPos):
        super().__init__(shape = "square")
        self.color(random.choice(Car.colors))
        self.shapesize(stretch_len=size[0] / Car.defaultTurtleSize, stretch_wid=size[1] / Car.defaultTurtleSize)
        self.penup()
        self.goto(startPos)
        self.setheading(180) #it's only matter if the car has a nonsymmetric design
        self.midToSideX = size[0] / 2
        self.midToSideY = size[1] / 2

    def goLeft(self):
        self.goto(self.xcor() - Car.stepSize, self.ycor())
