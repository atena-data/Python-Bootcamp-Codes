from turtle import Turtle, Screen
import random

screen = Screen()
race_on = False

# turtles color list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# screen size in pixels
screen.setup(width=500, height=400)

# ask user for their input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win? Pick a color!\n"
                                                          "(red, orange, yellow, green, blue, purple): ")

# set turtles for the race
y_position = -175
for turtle_index in range(6):
    y_position += 50
    turtle = Turtle("turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_position)
    turtles.append(turtle)

if user_bet:
    race_on = True

while race_on:
    # move turtles at random pace
    for turtle in turtles:
        if turtle.xcor() >= 230:
            race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

# to keep the screen on
screen.exitonclick()
