import turtle
import pandas as pd

stateIndex = 0
states = ["Alabama",
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming',]

stateXY = []

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0,300)
pen.pendown()
pen.clear()
pen.write(f"{states[stateIndex]}")

def createCSV():
    global stateXY
    stateXY = "\n".join(stateXY)
    with open("statesXY.csv", mode="w") as f:
        f.write(stateXY)

def finish():
    createCSV()
    screen.bye()

def addRow(x, y):
    global stateIndex
    stateXY.append(f"{states[stateIndex]},{x},{y}")
    stateIndex += 1
    if stateIndex == len(states):
        createCSV()
        screen.bye()
    else:
        pen.clear()
        pen.write(f"{states[stateIndex]}")


screen.onclick(addRow)
screen.onkeypress(finish, "q")
screen.listen()

screen.mainloop()