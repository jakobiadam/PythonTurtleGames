import turtle
import random

colors = ["red", "green", "blue", "yellow", "black"]
positions = [[-230,-100], [-230,-50], [-230,0], [-230,50], [-230,100]]

def racersInit(num, colors, positions):
    racers = [turtle.Turtle(shape="turtle") for i in range(num)]
    for i in range(num):
        racers[i].color(colors[i])
        racers[i].turtlesize(1.5,1.5,1.5)
        racers[i].penup()
        racers[i].goto(positions[i])
    return racers

def stepRacers(racers, screen):
    random.shuffle(racers)
    for racer in racers:
        racer.forward(random.randint(0,10))
        if racer.pos()[0] >= 230:
            return racer.color()[0]
    return 0

def game(screen):
    screen.title("Turtle Race")
    screen.delay(20)
    choosenColor = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color:")
    if not choosenColor:
        return
    choosenColor = choosenColor.lower()

    racers = racersInit(5, colors, positions)

    winnerColor = 0
    while True:
        winnerColor = stepRacers(racers, screen)
        if winnerColor:
            break
    
    if winnerColor == choosenColor:
        screen.title("You won!")
    else:
        screen.title(f"You lost! The winner was the {winnerColor} turtle!")

def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)

    while True:
        game(screen)
        wantToPlay = screen.textinput("Do you want to play again?", "Yes (Y) / No (N):")
        if (not wantToPlay) or (wantToPlay.lower() != "y"):
            break
        screen.clear()

    screen.exitonclick()

if __name__ == "__main__":
    main()