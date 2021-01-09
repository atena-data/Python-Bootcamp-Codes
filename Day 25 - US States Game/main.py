import turtle as t
import pandas as pd

# screen preparation
screen = t.Screen()
turtle = t.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# read source file
data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()

score = 0
guessed_states = []

while score < 51:
    answer = screen.textinput(title=f"{score}/50 states correct", prompt="What's the next state's name?").title()

    # give user an option to exit the game
    if answer == "Exit":
        break

    # check if user guess the state correctly
    if answer in state_list:
        row = data[data.state == answer]

        # update the map with user's response
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(row.x), int(row.y))
        turtle.write(f"{answer}", align="center", font=("Courier", 10, "normal"))
        score += 1
        guessed_states.append(answer)

# check the states that user couldn't guess
if len(guessed_states) < len(state_list):
    missing_states = [state for state in state_list if state not in guessed_states]


states_to_learn = pd.DataFrame(missing_states)
states_to_learn.to_csv("States_to_Learn.csv")
