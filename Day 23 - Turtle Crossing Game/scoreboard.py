from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto((0, 280))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL : {self.level}", align="center", font=("Courier", 10, "normal"))

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "bold"))

