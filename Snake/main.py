from food import Food
from scoreBoard import ScoreBoard
from snake import Snake

import turtle
import time

DELAY_ORIGINAL = 800

isFoodCollision = False
delay = int(DELAY_ORIGINAL / 3)
onGame = True
restart = False

screen = turtle.Screen()
screen.setup(width=620, height=620)
screen.bgcolor("black")
screen.tracer(False)
screen.title("Snake")
#screen.bgpic("yourname.gif")
name = screen.textinput("", "What is your name?")

snake = Snake()
foods = [Food() for _ in range(3)]
scoreBoard = ScoreBoard()

keysPressed = set()

actions = {
    "Up" : snake.w,
    "Down" : snake.s,
    "Left" : snake.a, 
    "Right" : snake.d
}

def setOnRestartTrue():
    global restart
    restart = True

screen.onkeypress(lambda : keysPressed.add("Up"), "Up")
screen.onkeypress(lambda : keysPressed.add("Down"), "Down")
screen.onkeypress(lambda : keysPressed.add("Left"), "Left")
screen.onkeypress(lambda : keysPressed.add("Right"), "Right")
screen.onkeyrelease(lambda : keysPressed.remove("Up"), "Up")
screen.onkeyrelease(lambda : keysPressed.remove("Down"), "Down")
screen.onkeyrelease(lambda : keysPressed.remove("Left"), "Left")
screen.onkeyrelease(lambda : keysPressed.remove("Right"), "Right")
screen.listen()

def game():
    global delay
    global isFoodCollision
    global onGame
    global restart
    global snake
    global foods
    global scoreBoard

    if onGame:
        for key in keysPressed:
            actions[key]()
            break

        if isFoodCollision:
            snake.moveTail()
            isFoodCollision = False
        else:
            snake.move()

        screen.update()

        if snake.testCollision():
            scoreBoard.gameOver()
            time.sleep(2)
            onGame = False
            scoreBoard.writeHighScore(name)
            scoreBoard.writeRestart()
            screen.ontimer(game, delay)
            return

        for food in foods:
            if snake.foodCollision(food):
                isFoodCollision = True
                scoreBoard.incrementScore(food.point)
                scoreBoard.writeScore()
                food.changePosition()
                delay = int(DELAY_ORIGINAL / len(snake.snake.queue))
                break

        screen.ontimer(game, delay)

    else:
        screen.onkeypress(setOnRestartTrue, "Return")
        if restart:
            onGame = True
            restart = False
            snake.newSnake()
            scoreBoard.startNewGame()
            foods[0].changePosition()
            foods[1].changePosition()
            foods[2].changePosition()
            delay = int(DELAY_ORIGINAL / len(snake.snake.queue))
            screen.update()

        screen.ontimer(game, 50)

def main():
    scoreBoard.writeScore()
    screen.update()
    time.sleep(1)

    game()

    screen.exitonclick()

if __name__ == "__main__":
    main()
