from turtle import Turtle,Screen

import pandas

screen=Screen()
turtle=Turtle()
screen.title("U.S States Game")

image="blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")

stateList=data["state"].to_list()

guessed_state=[]
missing_states=[]
while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="Whats another states name?").title()

    if answer_state=="Exit":
        missing_states=[state for state in stateList if state not in guessed_state]
        newData=pandas.DataFrame(missing_states)
        newData.to_csv("missing_states.csv")
        break
    if answer_state in stateList:
        guessed_state.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data["state"] == answer_state]
        x_cor = state_row["x"].item()
        y_cor = state_row["y"].item()
        t.goto(x_cor, y_cor)
        t.write(answer_state)

