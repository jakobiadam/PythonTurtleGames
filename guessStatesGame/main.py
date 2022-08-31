import pandas as pd
import turtle
import time

SCORE_FONT = ('Arial', 50, 'normal')

screen = turtle.Screen()
imageName = "blank_states_img.gif"
screen.addshape(imageName)
turtle.shape(imageName)
screen.tracer(0)
data = pd.read_csv("50_states.csv")

def createPen(x, y):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    return pen

def createStateWriter():
    stateDic = {}
    for _, row in data.iterrows():
        pen = createPen(row[1], row[2])
        pen.occurance = 0
        stateDic[row[0]] = pen
    return stateDic

def main():
    score = 0
    scorePen = createPen(0,300)
    stateDic = createStateWriter()

    while True:
        scorePen.clear()
        scorePen.write(f"Score : {score} / 50", align="center", font=SCORE_FONT)
        screen.update()
        time.sleep(1)

        if score >= 50:
            break

        answer = screen.textinput("Choose a state", "Say a state which you know: \n(Type exit to finish the game)")
        if answer in stateDic:
            if stateDic[answer].occurance == 0:
                stateDic[answer].write(f"{answer}", align="center")
                score += 1
                stateDic[answer].occurance = 1
        elif answer == 'exit':
            break

    missedStates = [key for key in stateDic if stateDic[key].occurance == 0]
    #df = pd.DataFrame(missedStates)
    #df.to_csv("statesToLearn.csv")
    with open("missedStates.csv", mode="w") as f:
        f.write("\n".join(missedStates))

if __name__ == "__main__":
    main()
    screen.exitonclick()