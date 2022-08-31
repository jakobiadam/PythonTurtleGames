from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard

import turtle
import time

SCREEN_X = 950
SCREEN_Y = 850
PITCH_X = 800
PITCH_Y = 600
PADDLE_X = 20
PADDLE_Y = 100
BALL_SIZE = 15
PADDLE_1_START_XY = (-370, 0)
PADDLE_2_START_XY = (370, 0)
FRAME_DELAY_MS_ORIGINAL = 25
FRAME_DELAY_MS = FRAME_DELAY_MS_ORIGINAL
FRAME_DELAY_MIN = 8

#Init screen
screen = turtle.Screen()
screen.setup(width=SCREEN_X, height=SCREEN_Y)
screen.screensize(canvwidth=PITCH_X, canvheight=PITCH_Y, bg="black")
screen.title("PONG GAME")
turtle.tracer(0)

#Init the main objects of the game
paddle1 = Paddle(size=(PADDLE_X, PADDLE_Y), startingPos=PADDLE_1_START_XY, ymax=PITCH_Y/2, ymin=-PITCH_Y/2)
paddle2 = Paddle(size=(PADDLE_X, PADDLE_Y), startingPos=PADDLE_2_START_XY, ymax=PITCH_Y/2, ymin=-PITCH_Y/2)
ball = Ball(BALL_SIZE, -PITCH_X/2, PITCH_X/2, -PITCH_Y/2, PITCH_Y/2)
scoreBoard = ScoreBoard()

keysPressed = set()

actions = {
    "u1": paddle1.moveUp,
    "d1": paddle1.moveDown,
    "u2": paddle2.moveUp,
    "d2": paddle2.moveDown,
}

def drawPitch(left, up, right, down):
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.color("white")
    pen.goto(left, down)
    pen.pendown()
    pen.goto(left, up)
    pen.goto(right, up)
    pen.goto(right, down)
    pen.goto(left, down)
    pen.penup()
    pen.goto(0,down)
    pen.pendown()
    pen.goto(0,up)

def game(actions=actions, ball=ball, keysPressed=keysPressed, screen=screen):
    for action in keysPressed:
        actions[action]()

    global FRAME_DELAY_MS
    if ball.collisionPaddle(paddle1):
        FRAME_DELAY_MS = max(ball.bouncePaddle(paddle1, FRAME_DELAY_MS), FRAME_DELAY_MIN)
    if ball.collisionPaddle(paddle2):
        FRAME_DELAY_MS = max(ball.bouncePaddle(paddle2, FRAME_DELAY_MS), FRAME_DELAY_MIN)
    if ball.collisionSide():
        ball.bounceSide()
    if ball.collisionBorder():
        scoreBoard.incrementScore(ball.pos()[0])
        scoreBoard.writeScores()
        if scoreBoard.win():
            return
        ball.start()
        FRAME_DELAY_MS = FRAME_DELAY_MS_ORIGINAL
        time.sleep(1)

    ball.move()
    screen.update()
    screen.ontimer(game, FRAME_DELAY_MS)

def main():

    drawPitch(-PITCH_X/2, PITCH_Y/2, PITCH_X/2, -PITCH_Y/2)
    scoreBoard.writeScores()
    screen.update()
    time.sleep(1)

    screen.onkeypress(lambda : keysPressed.add("u1"), "w")
    screen.onkeypress(lambda : keysPressed.add("d1"), "s")
    screen.onkeypress(lambda : keysPressed.add("u2"), "Up")
    screen.onkeypress(lambda : keysPressed.add("d2"), "Down")
    screen.onkeyrelease(lambda : keysPressed.remove("u1"), "w")
    screen.onkeyrelease(lambda : keysPressed.remove("d1"), "s")
    screen.onkeyrelease(lambda : keysPressed.remove("u2"), "Up")
    screen.onkeyrelease(lambda : keysPressed.remove("d2"), "Down")
    screen.listen()

    game()

    screen.exitonclick()

if __name__ == "__main__":
    main()
