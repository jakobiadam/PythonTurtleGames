from car import Car
from player import Player
from scoreBoard import ScoreBoard

from queue import Queue
import turtle
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_X_APPEARANCE = SCREEN_WIDTH / 2 + 100
CAR_SIZE = (70, 30)
LEVEL_POS = (-340, 225)
PLAYER_STARTING_POS = (0, -250)
PLAYER_SIZE = (30, 30)
DELAY_IN_MS = 100

cnt = 0
onGame = True

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("gray")
turtle.tracer(0)

cars = Queue(maxsize=1000)
player = Player(PLAYER_SIZE, PLAYER_STARTING_POS, "turtle", "green")
scoreBoard = ScoreBoard(levelPos=LEVEL_POS)

actions = {"Up" : player.moveUp}
keysPressed = set()
screen.onkeypress(lambda : keysPressed.add("Up"), "Up")
screen.onkeyrelease(lambda : keysPressed.remove("Up"), "Up")
screen.listen()

def zigZagLine(pen, length, heading, zigZagLength = 10):
    pen.setheading(heading)
    for i in range(0, length // zigZagLength):
        if (i % 2) == 0:
            pen.pendown()
        else:
            pen.penup()
        pen.forward(zigZagLength)

def createHighway():
    pen = turtle.Turtle()
    pen.penup()
    pen.color("white")
    pen.goto(-SCREEN_WIDTH / 2, -200)
    pen.pendown()
    pen.goto(SCREEN_WIDTH / 2, -200)

    for y in range(-150, 151, 50):
        pen.penup()
        pen.goto(pen.xcor(), y)
        zigZagLine(pen, 800, (pen.heading() + 180) % 360)

    pen.penup()
    pen.goto(pen.xcor(), 200)
    pen.pendown()
    pen.goto(-pen.xcor(), 200)
    pen.penup()
    pen.goto(0, -290)
    pen.pendown()
    pen.write("START", align="center", font=('Arial', 50, 'normal'))
    pen.penup()
    pen.goto(0, 210)
    pen.pendown()
    pen.write("FINISH", align="center", font=('Arial', 50, 'normal'))
    pen.hideturtle()

def randomCars(xPos = CAR_X_APPEARANCE):
    for y in range(-175, 176, 50):
        if random.randint(1,8) == 1:
            cars.put(Car(CAR_SIZE, (xPos, y)))

def testCollision():
    for car in cars.queue:
        if player.collisionWithCar(car):
            return True
    return False

def removeCars():
    while True:
        if not cars.empty():
            if cars.queue[0].xcor() < -CAR_X_APPEARANCE:
                cars.get()
            else:
                break
        else:
            break

def gameLoop():
    global cnt
    global onGame
    global DELAY_IN_MS
    for key in keysPressed:
        actions[key]()

    cnt = cnt % 10
    if cnt == 0:
        randomCars()
        removeCars()
    for car in cars.queue:
        car.goLeft()

    if testCollision():
        onGame = False
        scoreBoard.writeGameOver()
        return
    if player.finish():
        scoreBoard.writeNewLevel()
        player.goto(PLAYER_STARTING_POS)
        DELAY_IN_MS = int(0.75 * DELAY_IN_MS)
        time.sleep(1)
    
    screen.update()
    cnt += 1
    screen.ontimer(gameLoop, DELAY_IN_MS)


def main():
    createHighway()
    scoreBoard.writeNewLevel()
    screen.update()

    gameLoop()

    screen.exitonclick()

if __name__ == "__main__":
    main()
